class ANP(object):
    def __init__(self, measurable, capital, dataset):
        self.M = measurable
        self.C = capital
        dataset = self.dataset

    @classmethod
    def begin(self):
        print('starting ANP..')
