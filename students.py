class student:
    def __init__(self,name,surname,arasinv,final):
        self.name = name
        self.surname = surname
        self.arasinv = arasinv
        self.final = final


    def ortalama(self):
        global arasinv
        global final
        return( arasinv + final )/2
    try:
        if ortalama < 100:
         print('iyi ortalama : A+')
        elif ortalama > 75 :
            print('iyi ortalama : B')
        else:
            print('ortalaman : C tekrar girmen lazim')
    except:
        print('yanlisin var iyi bak')

import os
f = open('Jerry','w')
