import pickle
from os import path


class Save:

    def __init__(self):
        if path.exists('data'):
            pickle_in = open('data', 'rb')
            self.file = pickle.load(pickle_in)
            pickle_in.close()
        else:
            self.file = {}

    def check(self, name):
        return name in self.file

    def add(self, name, value):
        self.file[name] = value

    def save(self):
        pickle_out = open('data', 'wb')
        pickle.dump(self.file, pickle_out)
        pickle_out.close()

    def load(self, name):
        try:
            return self.file[name]
        except KeyError:
            return 0
