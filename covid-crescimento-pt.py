#!/usr/bin/env python
# -*- coding: utf8 -*-

from datetime import datetime
from datetime import timedelta
import numpy as np
#import matplotlib.pyplot as plt
inicio = datetime(2020, 3, 2)
casos = np.array([2,4,6,9,13,21,30,39,41,59,78,112,169,245,331,448,642,785])
# print (len(casos), ' casos: ', casos)

coef1, coef2 = np.polyfit(range(len(casos)), np.log(casos), 1)
# print ('coeficientes soft e hard', coef1, coef2)

print("   data        casos   dif  crescimento  projeção")

diff         = 0
diff_porcent = 0

for i in range(len(casos)):
    if (i > 0):
        diff = casos[i] - casos[i-1]
        diff_porcent = (diff / casos[i-1]) * 100

    print("%2s  %8d  %4d     %5.1f%%    %8.0f" % ((inicio + timedelta(days = i)).strftime("%Y-%m-%d"), casos[i], diff, diff_porcent, np.exp(coef2) * np.exp(coef1 * i)))

'''
Projeção básica: aplicar o coeficiente
'''
print("%2s                               %8.0f" % ((inicio + timedelta(days = i + 1)).strftime("%Y-%m-%d"), np.exp(coef2) * np.exp(coef1 * (i + 1))))
