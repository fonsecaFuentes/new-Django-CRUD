from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, get_user_model
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from .forms import SetPasswordForm
from .forms import PasswordResetForm
from .forms import UserForm, ProfileForm
from django.db.models.query_utils import Q


# Create your views here.
def home(request):
    messages_from_session = messages.get_messages(request)
    messages_list = []
    for message in messages_from_session:
        messages_list.append(message)
    context = {
        'messages': messages_list,
    }
    return render(request, 'home.html', context)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request, "Gracias por la confirmación por correo electrónico.\
            Ahora puedes iniciar sesión en tu cuenta."
        )
        return redirect('login')
    else:
        messages.error(request, "¡El enlace de activación no es válido!")

    return redirect('home')


def sing_up(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(
                request, user,
                user_creation_form.cleaned_data.get('email')
            )
            return redirect('home')
        else:
            data['form'] = user_creation_form
    return render(request, 'registration/register.html', data)


def activateEmail(request, user, to_email):
    email_subject = "Activa tu cuenta de usuario."
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    message = render_to_string('registration/template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': uidb64,
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(email_subject, message, to=[to_email])
    email.content_subtype = 'html'
    if email.send():
        messages.success(
            request, f'Estimado <b>{user}</b>, por favor ve a tu bandeja de\
            entrada del correo electrónico <b>{to_email}</b> y haz clic en el\
            enlace de activación recibido para confirmar y completar el\
            registro. <b>Nota:</b> Verifica tu carpeta de spam.'
        )
    else:
        messages.error(
            request, f'Problema al enviar el correo electrónico a {to_email},\
            verifica si lo has escrito correctamente.'
        )


@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu contraseña ha sido cambiada")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(
        request, 'registration/password_change.html', {'form': form}
    )


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(
                email=user_email)
            ).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string(
                    "registration/template_reset_password.html",
                    {'user': associated_user,
                     'domain': get_current_site(request).domain,
                     'uid': urlsafe_base64_encode(
                        force_bytes(associated_user.pk)
                     ),
                     'token': account_activation_token.make_token(
                        associated_user
                     ), "protocol": 'https' if request.is_secure() else 'http'}
                )
                email = EmailMessage(
                    subject, message, to=[associated_user.email]
                )
                email.content_subtype = 'html'
                if email.send():
                    messages.success(
                        request, "<h2>Restablecimiento de contraseña enviado\
                        </h2><hr><p>Te hemos enviado por correo \
                        electrónico las instrucciones para establecer \
                        tu contraseña, si existe una cuenta asociada a \
                        la dirección de correo que ingresaste. \
                        Deberías recibirlo en breve.<br>Si no recibes el \
                        correo electrónico, asegúrate de haber ingresado la \
                        dirección con la que te registraste y revisa tu \
                        carpeta de correo no deseado (spam).</p>"
                    )
                else:
                    messages.error(
                        request,
                        "Problema al enviar el correo electrónico \
                        de restablecimiento de contraseña, \
                        <b>PROBLEMA DEL SERVIDOR</b>"
                    )

            return redirect('home')

    form = PasswordResetForm()
    return render(
        request=request,
        template_name="registration/password_reset.html",
        context={"form": form}
    )


def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Tu contraseña ha sido establecida. \
                    Ahora puedes proceder a <b>iniciar sesión</b>."
                )
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(
            request, 'registration/password_reset.html', {'form': form}
        )
    else:
        messages.error(request, "El enlace ha caducado")

    messages.error(
        request, 'Algo salió mal. Redireccionando de vuelta \
        a la página de inicio'
    )
    return redirect("home")


# Pagina de perfil
@login_required
def profile(request):
    user = request.user
    user_form = UserForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    return render(request, 'profile/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def observations(request):
    return render(request, 'observations.html')


@login_required
def exit(request):
    logout(request)
    return redirect('home')
