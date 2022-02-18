from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do angulo: '))
print('sen {}: {:.2f} / cos {}: {:.2f} / tan {} : {:.2f}'.format(angulo, sin(radians(angulo)), angulo, cos(radians(angulo)), angulo, tan(radians(angulo))))
