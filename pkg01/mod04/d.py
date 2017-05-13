
from ...config import conf

def myname():
    return 'get {} from mod04'.format(conf.myname())

if __file__ == '__main__':
    print(myname())
