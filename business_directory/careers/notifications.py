import admin_notifications
from models import JobPost

def notification():
    not_approved_jp = JobPost.objects.filter(approved=False).count()
    if not_approved_jp:
        return "You have %s no approved job post%s.<br>You can approve them using the <a href='/admin/careers/jobpost/'>Job post Manager</a>." % (not_approved_jp, "s" if not_approved_jp>1 else "")
    else:
        return ''

admin_notifications.register(notification)