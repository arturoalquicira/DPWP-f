
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass

class Festival(object):
    def __init__(self):
        super(Festival, self).__init__()

        self._stage = ""
        self._headliner = ""
        self._opening_act = ""
        self.__show_time = 0

    @property
    def show_time(self):
        return self.__show_time


class Stage1(object):
    def __init__(self):
        self._stage = "Volcom Stage"
        self._headliner = "The Strokes"
        self._opening_act = "The Cribs"
        self.__show_time = 12

    @property
    def show_time(self):
        return self.__show_time


class Stage2(object):
    def __init__(self):
        self._stage = "Vans Stage"
        self._headliner = "Kings Of Leon"
        self._opening_act = "Friendly Fires"
        self.__show_time = 11

    @property
    def show_time(self):
        return self.__show_time

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
