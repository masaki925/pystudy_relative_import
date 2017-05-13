
from mod01 import a

def myname():
    return 'get {} from sub_02'.format(a.myname())

if __name__ == '__main__':
    print(myname())
