
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # fp = FormPage()
        # # pass info about inputs I want in the form
        # fp.inputs = {"first_name": "text", "last_name": "text", "Submit": "submit"}
        # fp.create_inputs()
        # self.response.write(fp.print_out("Enter your info: "))

        p = Page()
        p.body = "nothing"
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self._head = """
            <!DOCTYPE HTML>
            <html>
                <head>
                    <title></title>
                </head>
            <body>
            """

        self._body = """


            """
        self._close = """
            </body>
            </html>
            """
    @property
    def body(self):
        pass

    @body.setter
    def body(self, b):
        self._body = b


    def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        #run the instantiating function for the superclass
        #super for this class.... run it's __init__ function
        super(FormPage, self).__init__()

        self.__form_open = "<form method='GET'>"
        self.__form_close = "</form>"
        self.__inputs = dict()
        self.__input_string = ""

        # {"first_name": "text", "last_name": text}

    def create_inputs(self):
        for key, value in self.__inputs.iteritems():
            print key
            self.__input_string += '<input type="' + value + '" name = "' + key + '" />'

    def print_out(self, msg):
        return self._head + msg + self.__form_open + self.__input_string + self.__form_close + self._close

    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, dict):
        self.__inputs = dict

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
