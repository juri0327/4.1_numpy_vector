# -*- coding: utf-8 -*-

import numpy as np
from main import list2ndarray, dist, extract, drop
import unittest

class TestCase(unittest.TestCase):

    def test_list2ndarray(self):
        self.assertTrue(np.allclose(list2ndarray([0]), np.array([0])))
        self.assertTrue(np.allclose(list2ndarray([0.1, 1.0, 1.2]),
                                    np.array([0.1, 1.0, 1.2])))
        self.assertTrue(np.allclose(list2ndarray([-123, 53200, 9805, 208, 453]),
                                    np.array([-123, 53200, 9805, 208, 453])))

    def test_dist(self):
        self.assertEqual(float(dist(np.array([0., 1.]),
                                    np.array([0., 1.]))), 0)
        self.assertEqual(float(dist(np.array([0., 1.]),
                                    np.array([0., 0.]))), 1.)
        self.assertEqual(float(dist(np.array([0., 1.]),
                                    np.array([1., 0.]))), np.sqrt(2))

    def test_extract(self):
        self.assertTrue(np.allclose(extract(np.array([0, 1, 2, 3])),
                                    np.array([1, 2])))
        self.assertTrue(np.allclose(extract(np.array([0, 1, 32, 2, 3])),
                                    np.array([1, 32, 2])))
        self.assertTrue(np.allclose(extract(np.array([243590, 542760, 807, 50981534, 489])),
                                    np.array([542760, 807, 50981534])))

    def test_drop(self):
        self.assertTrue(np.allclose(drop(np.array([0, 1, 2, 3]), 0),
                                    np.array([0, 1, 2, 3])))
        self.assertTrue(np.allclose(drop(np.array([0, 1, 32, 2, 3]), 2),
                                    np.array([0, 1, 0, 2, 3])))
        self.assertTrue(np.allclose(drop(np.array([243590, 542760, 807, 50981534, 489]), 1),
                                    np.array([243590, 0, 807, 50981534, 489])))

if __name__ == "__main__":
    unittest.main()
