"""
Unit testing for lambdata package (example_module.py)
"""

import unittest

from oop_example import SocialMediaUser

from example_module import COLOR, increment

from random import randint

class SocialMediaUserTests(unittest.TestCase):
    """ Docstring """
    def setUp(self):
        self.user1 = SocialMediaUser('Nathan', 'Tennessee', '65')
        self.user2 = SocialMediaUser('Dante', 'Inferno')
    
    def test_name(self):
        """ Testing name attribute"""
        self.assertEqual(self.user1.name, 'Nathan')
    
    def test_location(self):
        """ Testing location attribute"""
        self.assertEqual(self.user2.location, 'Inferno')
    
    def test_is_popular(self):
        """ Testing is_popular method"""
        self.assertFalse(self.user1.is_popular())

        self.user1.receive_upvotes(randint(101, 1000))

        self.assertTrue(self.user1.is_popular())


class ExampleTest(unittest.TestCase):
    def test_increment(self):
        """ Testing increment function adds one """
        x0 = 0
        y0 = increment(x0)
        self.assertEqual(y0, 1)
        self.assertEqual(increment(100), 101)
        self.assertEqual(increment(-1), 0)
        self.assertEqual(increment(-0.5), 0.5)

if __name__ == "__main__":
    unittest.main()

