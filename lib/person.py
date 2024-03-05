#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__ (self,name="Guido", job="Sales"):
        self.name = name
        self.job = job


    def get_name(self):
        print("Retrieving name.")
        return self._name.title() if hasattr(self, '_name') else ''

    
    def set_name(self, name):
        if(type(name) == str  and 0 < len(name) <=25 ) :
            print("Job must be in list of approved jobs.")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
        


    name = property(get_name,set_name)
