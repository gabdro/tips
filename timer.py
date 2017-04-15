import time

class Timer(object):
    def __init__(self,f=None):
        self.f = f
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, type, value, tb):
        print('{} sec'.format(time.time() - self.start),file=self.f)