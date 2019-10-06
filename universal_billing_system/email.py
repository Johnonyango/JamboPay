from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_notification(name,email,amount,quantity):
    # Creating message subject and sender
    subject = 'Lipa deni'
    sender = 'j.yayah7@gmail.com'

    text_content = render_to_string('email/bill.txt',{ "name": name,"amount":amount,"quantity":quantity })
    html_content = render_to_string('email/bill.html',{ "name": name,"amount":amount,"quantity":quantity })

    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


