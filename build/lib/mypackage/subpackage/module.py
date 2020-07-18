import numpy as np
from mypackage.main import Gen
class summarize(Gen):
       def __init__ (self,size,nameDist,**kwargs):
              super().__init__(size,nameDist,**kwargs)
          
       def draw_sample(self):
             import matplotlib.pyplot as plt
             self.check_par()
             s=self.sample()
             count,bins,ignored=plt.hist(s,self.par[2], density=True)
             return plt.show()
     
       def descriptive_sample(self):
             self.check_par()
             s=self.sample()
             out_s=np.array([np.min(s),np.max(s),np.mean(s),np.std(s)])
             return out_s,print("Descriptive Method for "+ self.nameDist + " Distribution:","\n",'min:',np.min(s),'max:',np.max(s),'mean:',np.mean(s),'std:',np.std(s))



