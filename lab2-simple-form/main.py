
import webapp2
from page import MyPage

class MainHandler(webapp2.RequestHandler):

    def get(self):



        if self.request.GET:
            info = self.request.GET["first-name"] + ' ' + self.request.GET["last-name"]

            page = MyPage(self)
            self.response.write(page.print_contents(info))
        else:
            page = MyPage(self)
            self.response.write(page.print_contents())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
