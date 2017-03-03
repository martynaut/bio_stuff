import cherrypy
import uuid
from reverse_complement.revcom import rev_comp_change
from cherrypy.lib.static import serve_fileobj


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
