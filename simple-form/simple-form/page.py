class Page():

    #methods
    #behaviors - actions Store Code
    def __init__(self, main_self):
        #initializing function - CONSTRUCTOR
        #attributes
        #traits
        self.__id = 123456  # pretty private
        self._author = "Arturo"  # protected access
        self.title = "Welcome to the page"  # public access
        self.head = '''<!DOCTYPE HTML>

        <html>

            <head>
                <title>Simple Form</title>
                <link href="style.css" type="text/css" rel="stylesheet" />

            </head>
            <body>
            '''

        self.body = "Hello World"
        self.form = '''
            <form>
                <input type="text" name="first_name" />
                <input type="text" name="last_name" />
                <input type="submit" value="Enter" />


            </form>
        '''

        self.ender = '''
            </body>
        </html>
            '''

        #main_self is SCOPED to __init__
        main_self.response.write("blablabablal")

    def print_contents(self, i=''):
        if i=='':
            return self.head + self.body + self.form + self.ender
        else:
            return self.head + i + self.ender

class Button():
    def __init__(self):
        self.label = "Contact"
        self.size = 100