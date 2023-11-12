import seaborn as sns
from matplotlib import pyplot as plt


iris = sns.load_dataset('iris')  #数据采用自带的iris数据集
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)  #绘制散点图
plt.show()
sns.histplot(iris['sepal_length'], bins=10, kde=False) #绘制直方图
plt.show()
sns.boxplot(x='species', y='petal_length', data=iris) #绘制箱线图
plt.show()