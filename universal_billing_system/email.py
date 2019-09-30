<<<<<<< HEAD
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_notification(request):
    subject = 'Welcome to pabill by JamboPay'
    sender ='j.yayah7@gmail.com'

    text_content = render_to_string('email/notify.txt',{"name": name})
    html_content = render_to_string('email/notify.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
=======


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Lipa deni'
    sender = 'emmahg6@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/bill.txt',{"name": name})
    html_content = render_to_string('email/bill.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

>>>>>>> cbc84d9163904c4f2f31cdaa9413ee94ad588864
