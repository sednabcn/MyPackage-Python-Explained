""" Test functions for linalg module
"""
from __future__ import division, absolute_import, print_function

import warnings
import numpy as np
from unittest import TestCase
import mypackage
from mypackage.main import Gen
from mypackage.subpackage.module import summarize
from scipy.stats import ks_2samp


class Testmypackage(TestCase):
        
        def test_generated_samples(self):
            Size=[1000,1000,20000]
            NameDist=['Normal','Poisson','Binomial']
            Kwargs=[ {'mu':0,'sigma':0.1,'nn':30},{'mu':5,'sigma':None,'nn':14}, {'mu':9,'sigma':0.1,'nn':30}]
            Dv=[[-0.3259520071552185,0.3150695418383316,-0.005180066541565867,\
                 0.10228844738384534],[0,13,4.999,2.151975603950937],\
                [0,5,0.8937,0.8980536231205796]]
            Sarray=[np.array(rr) for rr in Dv]
            
            for size,nameDist,kwargs,sarray in zip(Size,NameDist,Kwargs,Sarray):         
                      s=summarize(size,nameDist,**kwargs).descriptive_sample()[0]
                      if self.assertTrue(ks_2samp(s,sarray)[1]>0.05):
                                summarize(size,nameDist,kwargs).draw_sample()
                      else:
                          "Raise Error Exception"
                      


