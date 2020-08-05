import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



x=10
y=20
def add(x,y):
    return x+y

    

def subtract(x,y):
    return x-y

x=30
y=20
add_result= add(x,y)
logger.info('Add:{}+{}={}'.format(x,y,add_result))
sub_result = subtract(x,y)
logger.info('subtract:{}-{}={}'.format(x,y,sub_result))