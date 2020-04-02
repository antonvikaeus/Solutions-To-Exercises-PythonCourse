#!/usr/bin/env python
class Person:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def printNameSubject(self):
		print(self.firstname, self.lastname)

class Student(Person):
	"""docstring for Student"""
	def __init__(self, firstname, lastname, subject):
		super().__init__(firstname, lastname)
		self.subject = subject

	def printNameSubject(self):
		print(self.firstname, self.lastname, self.subject)

class Teacher(Person):
    '''docstring for Teacher '''
    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course
            
    def printNameSubject(self):
        print(self.firstname, self.lastname, self.course)
