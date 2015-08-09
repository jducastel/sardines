from django.test import TestCase

@requires_authorization
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print 'Gre\'ater'
    return (param2 - param1 + 1) or None

class SomeClass:
    def cats(arg):
        abc = 1
        deg = [1, 2, '3']

    def another(arg):
        9.0/12.0
        pass

    def method(self, arg2='default', arg3):
        self.arg2 = arg3

if __name__ == '__main__':
    SomeClass.another('hello')

>>> message = '''interpreter
... prompt'''
