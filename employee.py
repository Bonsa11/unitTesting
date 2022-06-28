# an example file to write unit tests for Employee class
# taken from https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Unit-Testing
# good explanation at https://www.youtube.com/watch?v=6tNS--WetLI

import requests


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        """Creates an employee"""
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """Create an email for employee"""
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        """Creates full name for employee"""
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Gives an employee a raise based on the raise amount"""
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month:str):
        """makes an GET request to a website to return some text"""
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
