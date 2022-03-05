import numpy as np
import matplotlib.pyplot as plt
while True:
    try:   	
    	m1,m2,m3=map(int,input("Enter m1 m2 m3 (space separated integers) ").split())        
    	alpha = np.arange(0.0, 1.0, 0.01)
    	E1 = (alpha - m1 +m2+m3)**2 + (m1-m2+m3)**2 + (m1+m2-m3)**2 #from gamma to X
    	E2 = (1 - m1 + m2 + m3)**2 + (alpha/2 + m1 - m2 + m3)**2 + (m1 + m2 - m3)**2 #X to W
    	E3 = (1 - alpha/2 - m1 + m2 + m3)**2 + (0.5 + m1 - m2 + m3)**2 + (alpha/2 + m1 + m2 - m3)**2 # W to L
    	E4 = (-m1 + m2 + m3 + 0.5 - alpha/2)**2 + (m1 - m2 + m3 + 0.5 - alpha/2)**2 + (m1 + m2 - m3 + 0.5 - alpha/2)**2
    	
    	plt.subplot(1, 4, 1)
    	plt.plot(alpha, E1, '-')
    	plt.ylim((0, 5))
    	x = [0, 1]
    	labels1 = ['$\Gamma$', '$X$']
    	plt.xticks(x, labels1)
    	plt.ylabel('Normalized Energy')
    	
    	plt.subplot(1, 4, 2) 
    	plt.plot(alpha, E2, '-')
    	plt.ylim((0, 5))
    	plt.yticks([])
    	x = [0, 1]
    	labels1 = ['$X$', '$W$']
    	plt.xticks(x, labels1)
    	
    	plt.subplot(1, 4, 3)
    	plt.plot(alpha, E3, '-')
    	plt.ylim((0, 5))
    	plt.yticks([])
    	labels1 = ['$W$', '$L$']
    	plt.xticks(x, labels1)
    	
    	plt.subplot(1, 4, 4)
    	plt.plot(alpha, E4, '-')
    	plt.ylim((0, 5))
    	plt.yticks([])
    	labels1 = ['$L$', '$\Gamma$']
    	plt.xticks(x, labels1)
    	
    	#plt.show()
    	plt.draw()
    	plt.pause(0.001)
    except ValueError:
    	print ('ended by user')
    	break
