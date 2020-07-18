import mypackage
import numpy as np
from mypackage.main import Gen
from mypackage.subpackage.module import summarize


def mypackage_results(Size,NameDist,Kwargs):
    	return [[summarize(size,nameDist,**kwargs).descriptive_sample()[1],\
	summarize(size,nameDist,**kwargs).draw_sample()]  for size,nameDist,kwargs,sarray in zip(Size,NameDist,Kwargs)]
                   
if __name__=='__main__':
   Size=[1000,1000,20000]
   NameDist=['Normal','Poisson','Binomial']
   Kwargs=[{'mu':0.0,'sigma':0.1,'nn':30},{'mu':5,'sigma':None,'nn':14},{'mu':9,'sigma':0.1,'nn':30}]
   mypackage_results(Size,NameDist,Kwargs)
