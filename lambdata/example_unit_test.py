""" Unit Testing for lambdata package"""

import pandas as pd
import numpy as np
import unittest
import example_module as em

class LambdataTests(unittest.TestCase):
    def setUp(self):
        self.test_df = pd.DataFrame([[1, np.NaN], [np.NaN, np.NaN]])
        self.test_list = [1, 1]

    """ Testing lambdata package """
    def test_number_of_nulls(self):
        """ Testing number of nulls method """
        self.assertEqual(em.number_of_nulls(self.test_df), 3)
    
    def test_add_list_to_df(self):
        """ Testing add list to df """
        self.assertEqual(self.test_df.shape[1] + 1, em.add_list_to_df(self.test_list, self.test_df).shape[1])

if __name__ == "__main__":
    unittest.main()
