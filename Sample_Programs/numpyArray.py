# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:03:25 2018

@author: Ankit
"""

import numpy as np


def test_run():
    """print (np.array([2,3,4,5]))
    print (np.array([(2,3,4),(4,5,6)]))
    print (np.empty((5,4)))
    print (np.ones((5,4),dtype=np.int))
    print (np.random.random((5,4)))
    print (np.random.normal(5,4,size=(2,3)))
    print (np.random.randint(0,10,size=(5,4)))
    """
    np.random.seed(693)
    a=np.random.randint(0,10,size=(5))
#    print (a.size)
#    print (a.sum())
#    print (a.sum(axis=0))
#    print (a.sum(axis=1))
#    print (a.max(axis=0))
#    print (a.max(axis=1))
#    print (a.min(axis=0))
#    print (a.min(axis=1))
    
    print (a)
    mean = a.mean()
    print (mean)
    a[a<mean]=-4
    print (a)


if __name__  == "__main__":
    test_run()