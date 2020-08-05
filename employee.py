import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('emp.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:

    def __init__(self,fname,lname):
        self.fname= fname
        self.lname= lname
        logger.info('Created employee:{} {}'.format(self.fullname,self.email))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)

    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

emp1= Employee('vinay','satya')