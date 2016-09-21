import osnap.installer
import main

APPLICATION_NAME = 'app'
AUTHOR = 'test'

def make_installer(verbose):
    osnap.installer.make_installer(AUTHOR, APPLICATION_NAME, 'this is my test example', 'www.mydomain.com',
                                   [APPLICATION_NAME], '1.0.0', verbose=verbose)

if __name__ == '__main__':
    make_installer(True)
