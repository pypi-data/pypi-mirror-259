import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def send_email(sender_email, sender_password, subject, content, attachments, to_email_list, cc_email_list, smtp_server, smtp_port):
    sender_email = sender_email
    sender_password = sender_password
    subject = subject
    body = content
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(to_email_list)
    msg['Subject'] = subject
    if cc_email_list != []:
        msg['Cc'] = ", ".join(cc_email_list)

    msg.attach(MIMEText(body, 'plain'))

    if len(attachments)!=0:
        for filename in attachments:
            attachment = open(filename, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filename))
            msg.attach(part)

    server = smtplib.SMTP(smtp_server, smtp_port)  
    server.starttls()
    server.login(sender_email, sender_password)
    recipients = to_email_list + cc_email_list
    text = msg.as_string()
    server.sendmail(sender_email, recipients, text)

    server.quit()

