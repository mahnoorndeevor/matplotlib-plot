import matplotlib.pyplot as plt
A=[1000, 2000, 3000, 4000]
B=[10, 20, 30, 40]
plt.plot(A,B,marker='o',ms=7,mfc='g',mec='y',linestyle='dotted',color='r') #mec is outline of marker and mfc is the in color if want to do both color same then use mr='any color'
#for linestyle can also use ls=':'
plt.xscale('log')
plt.yscale('log')
plt.grid(ls=':',color='b',linewidth=1)
plt.show()