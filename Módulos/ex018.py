import math
a=float(input('Digite o ângulo que você deseja:'))
seno=math.sin(math.radians(a))
coseno=math.cos(math.radians(a))
tangente=math.tan(math.radians(a))
print("O seno de {} é {:.2f}.".format(a,seno))
print("O coseno de {} é {:.2f}.".format(a,coseno))
print("A tangente de {} é {:.2f}.".format(a, tangente))