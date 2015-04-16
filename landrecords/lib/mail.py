# -*- coding: utf-8 -*-

import smtplib
import mimetypes
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from landrecords.config import Config
from landrecords.lib.log import Log


class Mail(object):

    def __init__(self,
                 subject="Land records summary",
                 body="Here is your email",
                 frm='tthoren@thelensnola.org',
                 to=['tthoren@thelensnola.org']):

        log.debug('Mail')

        self.subject = subject
        self.body = body
        self.frm = frm
        self.to = to

    def send_email(self, msg):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(Config().GMAIL_USERNAME,
                Config().GMAIL_PASSWORD)
        s.sendmail(self.frm, self.to, msg.as_string())
        s.quit()

    def add_headers(self, msg):
        msg['Subject'] = self.subject
        msg['From'] = self.frm
        msg['To'] = ','.join(self.to)

        return msg

    def send_as_text(self):
        msg = MIMEText(self.body)

        msg = self.add_headers(msg)

        self.send_email(msg)

    def send_with_attachment(self, files=None):
        msg = MIMEMultipart(self.body)

        msg = self.add_headers(msg)

        for f in files:
            content_type, encoding = mimetypes.guess_type(f)

            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'
            main_type, sub_type = content_type.split('/', 1)
            fp = open(f, 'rb')
            message = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()

            message.add_header('Content-Disposition',
                               'attachment',
                               filename=basename(f))

            msg.attach(message)

        self.send_email(msg)

    def send_as_html(self):
        msg = MIMEMultipart('alternative')

        msg = self.add_headers(msg)

        html = (
            '<!DOCTYPE html><html><head><meta charset="utf-8"></head>' +
            '<body>' +
            self.body +
            '</body></html>')

        msg_text = MIMEText(html, 'plain')
        msg_html = MIMEText(html, 'html')

        msg.attach(msg_text)
        msg.attach(msg_html)

        self.send_email(msg)

if __name__ == '__main__':
    log = Log('initialize').initialize_log()
