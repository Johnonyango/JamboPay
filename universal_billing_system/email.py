from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_notification(name, email):
    subject = 'Welcome to pabill by JamboPay'
    sender ='j.yayah7@gmail.com'

    text_content = render_to_string('email/bill.txt',{ "name": name })
    html_content = render_to_string('email/bill.html',{ "name": name })

    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
