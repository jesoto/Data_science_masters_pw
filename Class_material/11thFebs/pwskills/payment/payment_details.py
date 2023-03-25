
import os,sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__),'..')))


def payment():
    print("this is ny payment file")
    
from course import course_details
course_details.course()