from rest_framework import serializers

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "http://127.0.0.1:4200/confirm-password/?token={}".format(reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Authentication Component"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    
    )
    