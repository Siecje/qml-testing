import osnap.installer
import main

APPLICATION_NAME = 'app'
AUTHOR = 'test'

PY_VERSION = '3.5.2'

def make_installer(verbose):
    osnap.installer.make_installer(PY_VERSION, APPLICATION_NAME, AUTHOR, 'this is my test example', 'www.mydomain.com',
                                   compile_code=True)

if __name__ == '__main__':
    make_installer(True)
