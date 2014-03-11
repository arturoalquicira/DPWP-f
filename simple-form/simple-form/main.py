
import webapp2   # what handles going to a browser
from page import Page

#master class
class MainHandler(webapp2.RequestHandler):

    #unique ti framework...
    #THIS FUNCTION RUNS FIRST!! CATALYST
    def get(self):

        #start writing the code


        if self.request.GET:
            info = self.request.GET["first_name"] + ' ' + self.request.GET["last_name"]

            page = Page(self)  # creates a page object
            self.response.write(page.print_contents(info))
        else:
            page = Page(self)  # creates a page object
            self.response.write(page.print_contents())

#associates class with framework
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
