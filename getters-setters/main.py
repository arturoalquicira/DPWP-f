
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.t = Transcript()
        self.t.grade1 = 90
        self.t.grade2 = 100
        self.t.quiz1 = 75
        self.t.quiz2 = 99
        self.t.calc_grade()  # run the calc_grade function
        self.t.final_grade += 5  # @x.setter
        print self.t.final_grade  # @property



class Transcript(object):  # the "object" inheritance is important
    def __init__(self):
        self.grade1 = 0
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.__final_grade = 0  # private property
        # self.__final_grade = self.calc_grade()  # calculate the grade

        # make final_grade a property

    @property
    def final_grade(self):
        return self.__final_grade

    @final_grade.setter  # this allows write access
    def final_grade(self, grade):
        self.__final_grade = grade

    def calc_grade(self):
        avg = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2)/4
        self.__final_grade = avg




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
