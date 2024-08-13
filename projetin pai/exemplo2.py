import matplotlib.pyplot
import matplotlib.pyplot as plt

y = [1, 2, 3, 4, 5, 6, 7, 8]
x = [10, 20, 30, 40, 50, 60, 70, 80]

plt.plot(x, y, marker= 'o', linestyle= '--', color= 'b' )

plt.ylabel('eixo Y')
plt.xlabel('eixo X')

plt.title('grafico, linha simples')


plt.show()