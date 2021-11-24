from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        "sitetitle": getattr(settings, "SITE_NAME", "SimplySaaS"),
        "current_user": reset_password_token.user,
        "email": reset_password_token.user.email,
        "resetlink": "{}{}?token={}".format(
            settings.FRONTEND_URL,
            settings.FRONTEND_RESET_PASSWORD_PATH,
            reset_password_token.key,
        ),
    }

    # render email text
    email_plaintext_subject = render_to_string(
        "usermanagement/user_reset_password_subject.txt", context
    ).strip()
    email_plaintext_message = render_to_string(
        "usermanagement/user_reset_password_body.txt", context
    )
    email_html_message = render_to_string(
        "usermanagement/user_reset_password_body.html", context
    )

    msg = EmailMultiAlternatives(
        subject=email_plaintext_subject,
        body=email_plaintext_message,
        from_email=getattr(settings, "SERVER_EMAIL", "noreply@somehost.local"),
        to=[reset_password_token.user.email],
    )
    # msg.attach_alternative(email_html_message, "text/html")
    msg.send()
    print("msg sent")
    pass