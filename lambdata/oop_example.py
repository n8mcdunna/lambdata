'''OOP Examples for Unit 3 Sprint 1 Module 2'''

import pandas as pd
import numpy as np

class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]

class BareMinimumClass:
    pass

class Complex:
    def __init__(self, real, imag):
        '''
        Constructor for complex numbers.
        Numbers have real and imaginary parts.
        '''
        self.r = real
        self.i = imag
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i
    def __repr__(self):
        return '({}, {}i)'.format(self.r, self.i)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)
    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes
    def is_popular(self):
        '''Return a boolean'''
        return self.upvotes > 100

class Animal:
    '''General representation of animals'''
    def __init__(self, name, weight, diet):
        self.name = str(name)
        self.weight = float(weight)
        self.diet = diet
    def run(self):
        return 'Run run run'
    def eat(self, food):
        return 'Fan of ' + str(food)
    
class Sloth(Animal):
    def __init__(self, name, weight, diet, naps):
        super().__init__(name, weight, diet)
        self.naps = int(naps)
    def say_something(self):
        return 'I am a sloth saying something'
    def run(self):
        return 'I am a sloth. I do not run!'


if __name__ == '__main__':
    num1 = Complex(3, 5)
    num2 = Complex(4, 2)
    num1.add(num2)

    user1 = SocialMediaUser('Nathan', 'Chattanooga')
    user2 = SocialMediaUser('Justin', 'Provo', 101)
    user3 = SocialMediaUser('Carl', 'Costa Rica', '50')
    print('is popular: {}, num upvotes: {}'.format(user2.is_popular(), user2.upvotes))
    print('is popular: {}, num upvotes: {}'.format(user3.is_popular(), user3.upvotes))
