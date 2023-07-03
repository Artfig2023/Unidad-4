class Imaginario:
    def __init__(self,real,imaginario):
        self.real = real
        self.imaginario = imaginario
    def __add__(self,other):
        if isinstance(other,Imaginario):
            first = '({} + {})'.format(self.real,other.real)
            second = '({} + {})'.format(self.imaginario, other.imaginario)
            return '{},{}'.format(first,second)
        else:
            raise ValueError('Not Imaginary')
    def __sub__(self,other):
        if isinstance(other,Imaginario):
            first = '({} - {})'.format(self.real,other.real)
            second = '({} - {})'.format(self.imaginario, other.imaginario)
            return Imaginario(first,second)
        else:
            raise ValueError('Not Imaginary')
    def __mul__(self,other):
        if isinstance(other,Imaginario):
            first = '({} * {}) - ({} * {})'.format(self.real,other.real,self.imaginario,other.imaginario)
            second = '({} * {}) - ({} * {})'.format(self.real,other.imaginario,other.real,self.imaginario)
            return Imaginario(first,second)
        else:
            raise ValueError('Not Imaginary')
    def __truediv__(self,other):
        if isinstance(other,Imaginario):
            w = '(({} * 2) + ({} * 2))'.format(other.real,other.imaginario)
            real = '({} * {}) + ({} * {}) / {}'.format(self.real,other.real,self.imaginario,other.imaginario,w)
            other = '({} * {}) + ({} * {}) / {}'.format(self.imaginario,other.real,self.real,other.imaginario,w)
            return Imaginario(real,other)
        else:
            raise ValueError('Not Imaginary')