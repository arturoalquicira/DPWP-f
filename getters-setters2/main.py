
import webapp2
# from DOCUMENT import CLASS
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.page = Page()  # triggers __init__ in Page class
        self.page.title = "Contact Us"
        self.response.write(self.page.all)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
