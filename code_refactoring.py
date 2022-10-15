import email
import smtplib
import imaplib
from email.header import decode_header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configparser import ConfigParser
import base64


class Email_handling:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, my_email: str, password: str, header=None):

        self.my_email = my_email
        self.password = password
        self.header = header

    def send_message(self, text_msg: str, recipients: list, subject=None):
        msg = MIMEMultipart()
        msg['From'] = self.my_email
        msg['To'] = ','.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(text_msg))

        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.my_email, self.password)
        ms.sendmail(login, msg['To'], msg.as_string())
        ms.quit()

    def receive_latest_msg(self, header=None) -> email:
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.my_email, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else "ALL"
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        res, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message

    def receive_msg_properties(self, header=None):
        msg = self.receive_latest_msg(header)
        sender = decode_header(msg['From'])[0][0]
        if type(sender) is bytes:
            sender = sender.decode()
        subject = decode_header(msg['Subject'])[0][0]
        if type(subject) is bytes:
            subject = subject.decode()
        date = msg['Date']
        return sender, subject, date

    def receive_msg_text(self, header=None):
        msg = self.receive_latest_msg(header)
        for part in msg.walk():
            if part.get_content_maintype() == 'text' or part.get_content_subtype() == 'plain':
                content = base64.b64decode(part.get_payload()).decode()
                return content


if __name__ == '__main__':
    parser = ConfigParser()
    parser.read('authorization.ini')
    login = parser['log_pass']['login']
    app_pass = parser['log_pass']['password']

    text = 'This is the third test for sending message'

    emailing = Email_handling(login, app_pass)
    # emailing.send_message(text, ['salegroup78@mail.ru'])

    # print(emailing.receive_msg_properties('Practice Coding with String Split and Join'))
    # print(emailing.receive_msg_properties('Test message'))
    # print(emailing.receive_msg_properties())

    # print(emailing.receive_msg_text('Practice Coding with String Split and Join'))
    # print(emailing.receive_msg_text("Test message"))
    print(emailing.receive_msg_text())
