class Navigator:
    # TODO: store navigaton history in array (limit for example to 10 items)
    #       -> implement methods 'undo(step)' and maybe 'redo(step)' too
    
    def __init__(self):
        self.divider, self.end = '>', '>'
        self.navigation = []

    def set_divider(self, divider):
        self.divider = divider

    def set_end(self, ender):
        self.end = ender

    def navigate(self, location):
        self.navigation.append(location)

    def down(self, step=1):
        self.navigation = self.navigation[:-step]

    def clean(self):
        self.navigation = []

    def getLocation(self):
        return self.divider.join(self.navigation) + self.end