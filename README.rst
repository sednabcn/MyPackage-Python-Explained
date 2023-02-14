===========
Mypackage
===========

Mypackage provides a method to generate random distribution samples based on
the Normal, Poisson and Binomial distribution. Typical usage
often looks like this::

    #!/usr/bin/env python

    from mypackage import srcipt-command_line
    from mypackage import Gen
    from mypackage.subpackage.module import draw_sample, descriptive_sample

Installation
------------
-Download the package from https://github.com/sednabcn/Python-Package-Explained
-Make the dir MyPackage and put into it all files downloaded
Install locally: pip3 install .
Install to the system: sudo python setup.py install


mypackage
--------

To use (with caution), simply do::
sedna@hp:~$ python3.8
Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mypackage
>>> import mypackage.subpackage
>>> import mypackage.tests
>>> import mypackage.subpackage.module
>>> from mypackage.main import Gen
>>> from mypackage.subpackage.module import summarize

test_generated_samples (mypackage.tests.test_mypackage.Testmypackage) ... ok

----------------------------------------------------------------------
Ran 1 test in 1.897s

OK


script
------
To use at the prompt (command-line)
sedna@hp:$ script-command_line --Normal 1000 0.0 0.1 30 --Poisson 1000 5 None 14 --Binomial 20000 9 0.1 30 
Descriptive Method for Normal Distribution: 
 min: -0.3499113924055577 max: 0.30747293791217245 mean: -0.004195217226063487 std: 0.10254739392393213
Descriptive Method for Poisson Distribution: 
 min: 0 max: 16 mean: 4.941 std: 2.224751446791304
Descriptive Method for Binomial Distribution: 
 min: 0 max: 6 mean: 0.89995 std: 0.89528766187187
