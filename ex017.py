from math import sqrt
catop = float(input('Digite o tamanho do cateto oposto: '))
catadj = float(input('Digite o tamanho do cateto adjacente: '))
hipot = sqrt(catop**2 + catadj**2)
print('A hipotenusa desse triângulo vale : {}'.format(hipot))
