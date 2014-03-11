class MyPage():


    def __init__(self, main_self):


        self._author = "Arturo Alquicira"
        self.title = "Lab 2 - Simple Form"
        self.head = '''<!DOCTYPE HTML>

        <html>

            <head>
                <title>Lab2 - Simple Form</title>
                <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.4.2/pure-min.css">

                <link href="style.css" type="text/css" rel="stylesheet" />

            </head>
            <body>
            '''

        self.body = ""
        self.form = '''
            <div class="pure-g">
    <div id="wrapper" class="pure-u-1-1">

        <h1>Student Info</h1>

        <form id="student-form" class="pure-form">

        <fieldset class="pure-group">
            <input type="text" class="pure-input-1-4" name="first-name" placeholder="First Name"><br>
            <input type="text" class="pure-input-1-4" name="last-name" placeholder="Last Name"><br>
            <input type="text" class="pure-input-1-4" name="student-id" placeholder="Student ID"><br>
        </fieldset>


        <label for="option-one" class="pure-checkbox">
            <input id="option-one" type="checkbox" value="Car">
            Car
        </label>
        <label for="option-two" class="pure-checkbox">
            <input id="option-two" type="checkbox" value="Motorbike">
            Motorbike
        </label>
        <label for="option-three" class="pure-checkbox">
            <input id="option-three" type="checkbox" value="Bicycle">
            Bicycle
        </label>
        <label for="option-four" class="pure-checkbox">
            <input id="option-four" type="checkbox" value="None">
            None
        </label>


        <label for="option-five" class="pure-radio">
            <input id="option-five" type="radio" name="optionsRadios" value="Male" checked>
            Male
        </label>
        <label for="option-six" class="pure-radio">
            <input id="option-six" type="radio" name="optionsRadios" value="Female" checked>
            Female
        </label>

            <select class="pure-input-1-4">
                <option value="DAD">Digital Arts & Design</option>
                <option value="WDD">Web Design & Development</option>
                <option value="CA">Computer Animation</option>
                <option value="GD">Game Development</option>
            </select><br>

        <button type="submit" class="pure-button pure-input-1-4 pure-button-primary">Submit</button>

    </form>
    </div>
</div>

        '''

        self.ender = '''
            </body>
        </html>
            '''

        # main_self.response.write("Your request was successful!")

    def print_contents(self, i=''):
        if i=='':
            return self.head + self.body + self.form + self.ender

        else:
            return self.head + i + self.ender

class Button():
    def __init__(self):
        self.label = "Contact"
        self.size = 100