

class AClass(object):
    def __init__(self, config):
        self.prop1 = config.prop1
        self.prop2 = config.prop2
        self.output = 0

    def run(self):
        self.output = self.prop1 + self.prop2
        return self.output
