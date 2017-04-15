import cherrypy
import uuid
from reverse_complement.revcom import rev_comp_change
from cherrypy.lib.static import serve_fileobj
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib


def send_email_results(email, files):

    msg = MIMEMultipart()
    msg['From'] = 'science <science@scienceisthenewblack.eu>'
    msg['To'] = 'scienceisthenewblack_user <'+email+'>'
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = 'Results from scienceisthenewblack'
    msg.attach(MIMEText('in the attachment file with the results\n\n' +
                        'scienceisthenewblack team'))
    for file in files:
        with open(file) as file_read:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(file_read.read().replace('<br />', '\n'))
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="'+file+'"')
            msg.attach(part)
    smtp = smtplib.SMTP("localhost")
    smtp.sendmail(
                  'mirnamotif <mirnamotif@scienceisthenewblack.eu>',
                  ['mirnamotif_user <'+email+'>'],
                  msg.as_string())
    smtp.close()


class Page:
    @cherrypy.expose
    def index(self):
        return open("science_html/home.html").read()

    @cherrypy.expose
    def rev_comp_site(self):
        html = open("science_html/rev_comp.html").read()
        return html.format(seq='put your sequence here', result='result')

    @cherrypy.expose
    def shutdown(self):
        cherrypy.engine.exit()

    @cherrypy.expose
    def rev_comp(self, change_type, NA, seq):
        seq_result = rev_comp_change(change_type, NA, seq)
        html = open("science_html/rev_comp.html").read()
        return html.format(seq=seq, result=seq_result)

if __name__ == "__main__":
    cherrypy.config.update("config.conf")
    cherrypy.quickstart(Page(), config="config.conf")
