import numpy as np
import matplotlib.pyplot as plt

rho = 7850
E = 2.1*10**11
L = 1.49
d = 1.38*10**-2
I = np.pi*d**4/64
A = np.pi*d**2/4

a = np.array([1.875, 4.694, 7.855, 10.996])
frec = a**2*np.sqrt(E*I/(rho*A*L**4))/(2*np.pi)

print('Primeras frecuencias normales')
for i in range(len(frec)):
    print(f'f{i + 1} = {frec[i]}')

a1 = np.array([1.875, 4.694])
frec_exp = np.array([4.8, 23.5])
E_exp = (frec_exp*2*np.pi/a1**2)**2*rho*A*L**4/I

print('Modulos de Young experimentales')
for i in range(len(frec_exp)):
    print(f'E{i + 1} = {E_exp[i]}')

print('Promedio de E')
print(f'{np.mean(E_exp)/1e11} +/- {np.std(E_exp)/1e11}')


b1 = plt.imread('Frec1.png')
b2 = plt.imread('Frec2.png')

valorx1 = np.linspace(60, 80, 10000)
valorx2 = np.linspace(0, 10, 10000)

plt.figure(figsize = (8, 8))
plt.imshow(b1, extent=[60, 80, -10, 10])
plt.xticks([60, 65, 70, 75, 80], [6.0, 6.5, 7.0, 7.5, 8.0])
plt.yticks([-10, -5, 0, 5, 10], [r'$-2 \times 10^3$', r'$-1 \times 10^3$', 0, r'$1 \times 10^3$', r'$2 \times 10^3$'])
plt.tick_params(labelsize = 12)
plt.xlabel(r'Tiempo ($s$)', fontsize = 15)
plt.ylabel(r'Amplitud', fontsize = 15)
plt.grid()

plt.figure(figsize = (8, 8))
plt.imshow(b1, alpha = 0.5, extent=[60, 80, -10, 10])
plt.plot(valorx1, 8*np.sin(valorx1*(2*np.pi*0.488) - 1.6), 'b-')
plt.xticks([60, 65, 70, 75, 80], [6.0, 6.5, 7.0, 7.5, 8.0])
plt.yticks([-10, -5, 0, 5, 10], [r'$-2 \times 10^3$', r'$-1 \times 10^3$', 0, r'$1 \times 10^3$', r'$2 \times 10^3$'])
plt.tick_params(labelsize = 12)
plt.xlabel(r'Tiempo ($s$)', fontsize = 15)
plt.ylabel(r'Amplitud', fontsize = 15)
plt.grid()

plt.figure(figsize = (8, 8))
plt.imshow(b2, extent=[0, 10.0, -5.0, 5.0])
plt.xticks([0, 2, 4, 6, 8, 10], [0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([-5, -2.5, 0, 2.5, 5], [r'$-3.0 \times 10^3$', r'$-1.5 \times 10^3$', 0, r'$1.5 \times 10^3$', r'$3.0 \times 10^3$'])
plt.tick_params(labelsize = 12)
plt.xlabel(r'Tiempo ($s$)', fontsize = 15)
plt.ylabel(r'Amplitud', fontsize = 15)
plt.grid()

plt.figure(figsize = (8, 8))
plt.imshow(b2, alpha = 0.5, extent=[0, 10.0, -5.0, 5.0])
plt.plot(valorx2, 4*np.sin(valorx2*(2*np.pi*0.48) + 4), 'b-')
plt.xticks([0, 2, 4, 6, 8, 10], [0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([-5, -2.5, 0, 2.5, 5], [r'$-3.0 \times 10^3$', r'$-1.5 \times 10^3$', 0, r'$1.5 \times 10^3$', r'$3.0 \times 10^3$'])
plt.tick_params(labelsize = 12)
plt.xlabel(r'Tiempo ($s$)', fontsize = 15)
plt.ylabel(r'Amplitud', fontsize = 15)
plt.grid()

plt.figure(figsize = (8, 8))
plt.imshow(b2, alpha = 0.5, extent=[0, 10.0, -5.0, 5.0])
plt.plot(valorx2, -2.5*np.sin(valorx2*(2*np.pi*2.85)), 'r-')
plt.xticks([0, 2, 4, 6, 8, 10], [0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.yticks([-5, -2.5, 0, 2.5, 5], [r'$-3.0 \times 10^3$', r'$-1.5 \times 10^3$', 0, r'$1.5 \times 10^3$', r'$3.0 \times 10^3$'])
plt.tick_params(labelsize = 12)
plt.xlabel(r'Tiempo ($s$)', fontsize = 15)
plt.ylabel(r'Amplitud', fontsize = 15)
plt.grid()

plt.show()