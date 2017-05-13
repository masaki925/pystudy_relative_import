
from ..mod01 import a

def myname():
    return 'get {} from mod02'.format(a.myname())

if __file__ == '__main__':
    print(myname())
