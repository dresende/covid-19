import numpy as np
#import matplotlib.pyplot as plt
dias = np.array([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
casos = np.array([2,4,6,9,13,21,30,39,41,59,78,112,169,245,331,448,642,785])
#print (len(dias), '  dias: ', dias)
#print (len(casos), ' casos: ', casos)

coef1, coef2 = np.polyfit(dias,np.log(casos),1)
print ('coeficientes soft e hard', coef1, coef2)

contador = 0
diff = 0
diff_porcent = 0
for dia in dias:
    if (contador > 0):
        diff = casos[contador] - casos[contador-1]
        diff_porcent = (diff / casos[contador-1]) * 100

    projecao = "%.0f" % (np.exp(coef2)*np.exp(coef1*dia))

    print (dia ,' ', casos[contador] , ' diferença: ' + str(diff) , ' taxa de crescimento:',  "%.1f" % diff_porcent  + '%' , ' (projeção:' + str(projecao) + ')' )
    contador = contador + 1


'''
Projeção básica: aplicar o coeficiente
'''
projecao = "%.0f" % (np.exp(coef2)*np.exp(coef1*(dia+1)))
print (dia + 1, ' ',  str(projecao) + " (projeção)")