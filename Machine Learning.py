
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA 
import matplotlib.cm as cm



#digits = load_digits()
#
#data = digits.data
#n_samples, n_features = data.shape
#n_digits = len(np.unique(digits.target))
#labels = digits.target
#
#
#pca = PCA(n_components=10)
#data_r = pca.fit(data).transform(data)
#a = pca.explained_variance_ratio_
#
#print('współczynnik wyjaśnionwych wariancji, 10 pozycji: %s' 
#      %(pca.explained_variance_ratio_))
#print('suma wsp. wyj. war. 10 pozycji: %s' 
#      %(sum(pca.explained_variance_ratio_)))
#
#x = np.arange(10)
#ys = [i+x+(i*x)**2 for i in range(10)]
#plt.figure()
#colors = cm.rainbow(np.linspace(0, 1, len(ys)))
#
#for c, i, target_name in zip(colors, [1,2,3,4,5,6,7,8,9,10], labels):
#    plt.scatter(data_r[labels == i, 0], data_r[labels == i, 1], alpha = 0.4)
#    plt.legend()
#    plt.title('Wykres przedstawia charakterystyki wariancji')
#    plt.show()

size=10
digits=load_digits()
#for i in range(size):
#    plt.gray()
#    plt.matshow(digits.images[i])
#    plt.show()
#size=10
#
#digits=load_digits()
#for i in range(size):
#    plt.gray()
#    plt.subplot(5,2)
#    plt.matshow(digits.images[i])
#    plt.show()
##
plt.figure()
for i in range(size):
    plt.subplot(2, 5, i+1)
    plt.imshow(digits.images[i])
#    