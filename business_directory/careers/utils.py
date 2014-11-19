from django_messages.models import Message


def send_apply_messsage(recipient, message, sender):
    # subject = self.cleaned_data['subject']
    msg = Message(
        sender = sender,
        recipient = recipient,
        subject = "",
        body = message,
    )
    msg.save()
    return msg