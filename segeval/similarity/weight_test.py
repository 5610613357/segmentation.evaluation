'''
Tests weight functions.

.. moduleauthor:: Chris Fournier <chris.m.fournier@gmail.com>
'''
import unittest
from . import (weight_s_scale, weight_t_scale)


class TestWeight(unittest.TestCase):
    '''
    Test similarity helper functions.
    '''
    # pylint: disable=R0904,C0103,C0324
    
    def test_weight_t_scale(self):
        '''
        Test to see that penalties for substitution edits are discounted from
        3 to 1.5.
        '''
        transpositions = [[1,2], [1,3], [1,4]]
        weight = weight_t_scale(transpositions, 4)
        self.assertEqual(weight, 1.5)
        

    def test_weight_s_scale(self):
        '''
        Test to see that penalties for transposition edits are discounted from
        3 to 1.5.
        '''
        substitutions = [[1,2], [1,3], [1,4]]
        weight = weight_s_scale(substitutions, 4)
        self.assertEqual(weight, 1.5)
        weight = weight_s_scale(substitutions, 5, 2)
        self.assertEqual(weight, 1.5)
