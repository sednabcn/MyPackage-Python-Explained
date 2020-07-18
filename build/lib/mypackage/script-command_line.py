#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:38:58 2020

@author: sedna
"""

import sys
from mypackage.subpackage.module import summarize

def mypackage_results(Size,NameDist,Kwargs):
    	return [[summarize(size,nameDist,**kwargs).descriptive_sample()[1],\
	summarize(size,nameDist,**kwargs).draw_sample()]  for size,nameDist,kwargs in zip(Size,NameDist,Kwargs)]


def main():
    script = sys.argv[0]
    actions = [sys.argv[n] for n in range(1,len(sys.argv),5)]
    assert script =='script-command_line.py'
    Size=[]
    NameDist=[]
    Kwargs=[]
    for action in actions:
            if   action == '--Normal':
                wargs={}
                NameDist.append('Normal')
                Size.append(int(sys.argv[2]))
                wargs.update({'mu':float(sys.argv[3])})
                wargs.update({'sigma':float(sys.argv[4])})
                wargs.update({'nn':int(sys.argv[5])})
                Kwargs.append(wargs)
            elif action=='--Poisson':
                wargs={}
                NameDist.append('Poisson')
                Size.append(int(sys.argv[7]))
                wargs.update({'mu':int(sys.argv[8])})
                wargs.update({'sigma':None})
                wargs.update({'nn':int(sys.argv[10])})
                Kwargs.append(wargs)
            elif action=='--Binomial':
                wargs={}
                NameDist.append('Binomial')
                Size.append(int(sys.argv[12]))
                wargs.update({'mu':int(sys.argv[13])})
                wargs.update({'sigma':float(sys.argv[14])})
                wargs.update({'nn':int(sys.argv[15])})
                Kwargs.append(wargs)
            else:
                print ("Rise Exception Error")

    return mypackage_results(Size,NameDist,Kwargs)

if __name__ == '__main__':
        main()
        """
        python3.8 script-command-line.py --Normal 1000 0.0 0.1 30 --Poisson 1000 5 None 14 --Binomial 20000 9 0.1 30 
        """
        
