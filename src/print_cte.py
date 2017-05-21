import pylab
from pylab import *
import numpy as np

# list_of_files = [ ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.05_d_0_i_0.txt', 'P-Ctrl (p=0.05)', 'r.'),
#                   ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.05_d_0.5_i_0.txt', 'PD-Ctrl (p=0.05, d=0.5)', 'g.'),
#                   ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.05_d_1.0_i_0.txt', 'PD-Ctrl (p=0.05, d=1.0)', 'b.'),
#                   ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_0.5_i_0.txt', 'PD-Ctrl (p=0.1, d=0.5)', 'y.'),
#                   ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_1.0_i_0.txt', 'PD-Ctrl (p=0.1, d=1.0)', 'k.'),
#                   ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_1.5_i_0.txt', 'PD-Ctrl (p=0.1, d=1.5)', 'c.'),
#                   ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_2.0_i_0.txt', 'PD-Ctrl (p=0.1, d=2.0)', 'm.')] #, ...

list_of_files = [ ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_1.5_i_0.txt', 'PID-Ctrl (p=0.1, d=1.5, i=0)', 'r.'),
                  ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_1.5_i_0.001.txt', 'PID-Ctrl (p=0.1, d=2.0, i=0.001)', 'g.'),
                  ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_1.5_i_0.005.txt', 'PID-Ctrl (p=0.1, d=2.0, i=0.005)', 'b.'),
                  ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_1.5_i_0.0025.txt', 'PID-Ctrl (p=0.1, d=2.0, i=0.0025)', 'y.'),
                  ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_1.5_i_0.0005.txt', 'PID-Ctrl (p=0.1, d=2.0, i=0.0005)', 'k.'),
                  ('/Users/robert/SDCND/Term2/CarND-PID-Control-Project/data/p_0.1_d_1.5_i_0.0001.txt', 'PID-Ctrl (p=0.1, d=2.0, i=0.0001)', 'c.')] #, ...


datalist = [ ( pylab.loadtxt(filename), label, symbol ) for filename, label, symbol in list_of_files ]

for data, label, symbol in datalist:
    pylab.plot( data[:,0], data[:,1], symbol, label=label )

pylab.plot((0, 3000), (0, 0), 'k-')

pylab.legend()
pylab.title("PDI-Controler")
pylab.xlabel("Time")
pylab.ylabel("CTE")

show()
