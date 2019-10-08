def send_message(name, email):
    subject = 'account created'
    sender = 'j.yayah7@gmail.com'

    text_content = render_to_string('email/bill.txt',{ "name": name })
    html_content = render_to_string('email/bill.html',{ "name": name })

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
