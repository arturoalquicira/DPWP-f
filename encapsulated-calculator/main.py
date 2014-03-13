
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.head = """
            <!DOCTYPE HTML>
            <html>
                <head>
                    <title></title>
                </head>
            <body>
            """

        self.body = """
                <h1>Arturo</h1>
                <p>Monday: </p> <p>{self.arturo.monday}</p>
                <p>Tuesday: </p> <p>{self.arturo.tuesday}</p>
                <p>Wednesday: </p> <p>{self.arturo.wednesday}</p>
                <p>Thursday: </p> <p>{self.arturo.thursday}</p>
                <p>Friday: </p> <p>{self.arturo.friday}</p>
                <strong>Total time:</strong> <p>{self.arturo.avg_exercise()}

            """
        self.end = """
            </body>
            </html>
            """
        self.all = self.head + self.body + self.end
        self.response.write(self.all)

        self.arturo = Timing()
        self.arturo.monday = 60
        self.arturo.tuesday = 40
        self.arturo.wednesday = 90
        self.arturo.thursday = 70
        self.arturo.friday = 80
        self.arturo.avg_exercise()

        self.austin = Timing()
        self.austin.monday = 30
        self.austin.tuesday = 20
        self.austin.wednesday = 90
        self.austin.thursday = 40
        self.austin.friday = 35
        self.austin.avg_exercise()
        
        self.sam = Timing()
        self.sam.monday = 22
        self.sam.tuesday = 58
        self.sam.wednesday = 45
        self.sam.thursday = 45
        self.sam.friday = 120
        self.sam.avg_exercise()
        
        self.bryan = Timing()
        self.bryan.monday = 30
        self.bryan.tuesday = 40
        self.bryan.wednesday = 50
        self.bryan.thursday = 20
        self.bryan.friday = 10
        self.bryan.avg_exercise()
        
        self.lyte = Timing()
        self.lyte.monday = 20
        self.lyte.tuesday = 30
        self.lyte.wednesday = 40
        self.lyte.thursday = 20
        self.lyte.friday = 90
        self.lyte.avg_exercise()

class Timing():
    def __init__(self):

        self.monday = 0
        self.tuesday = 0
        self.wednesday = 0
        self.thursday = 0
        self.friday = 0
        self.__final_time = 0


    @property
    def final_time(self):
        return self.__final_time

    @final_time.setter
    def final_time(self, time):
        self.__final_time = time

    def avg_exercise(self):
        avg = self.monday + self.tuesday + self.wednesday + self.thursday + self.friday
        self.__final_time = avg

        

        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
