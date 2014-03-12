
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.luke = Character()
        self.luke.name = "Luke"

        self.leia = Character()
        self.leia.name = "Leia"
        self.leia.age = self.luke.age
        self.leia.profession = "Princess"
        self.leia.speak()


        self.yoda = Character()
        self.yoda.name = "Yoda"
        self.yoda.age = 819
        self.yoda.profession = "Jedi"
        self.yoda.speak()

        for y in self.yoda.__dict__:
            print y

class Character():
    def __init__(self):
        # default values assigned here
        self.name = ""
        self.age = 0
        self.profession = ""

    def figth(self):
        print "Yeahh"

    def speak(self):
        print "How do yo do, my name is " + self.name





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
