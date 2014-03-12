class Page(object):
    def __init__(self):
        self.head = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>{self.title}</title>
            </head>
        <body>
        """

        self.body = """
            <a href="?fruit=strawberry">Strawberry</a>
            <a href="?fruit=orange">Orange</a>
            <a href="?fruit=banana">Banana</a>

        """
        self.close = """
        </body>
        </html>
        """

        self.all = self.head + self.body + self.close
        self.__title = "Welcome!"

        # property for __title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, name):
        self.__title = name
        #  reformat the string
        self.all =  self.all.format(**locals())