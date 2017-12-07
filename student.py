from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}


    def add_module(self,module):
        self.module = module
        self.modules.append(module)
        ## 5.

    def get_list_modules(self):
        for i in self.modules:
            return str(self.modules[i])

    def get_grades(self):
        for i in self.grades:
            return str(self.grades[i])


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
