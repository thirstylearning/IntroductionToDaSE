import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris


data = load_iris()
iris = pd.DataFrame(data=data.data, columns=data.feature_names) #采用iris数据集

plt.figure(figsize=(10,6)) #绘制折线图
plt.plot(iris['sepal length (cm)'])
plt.title('Sepal Length Line Plot')
plt.xlabel('Index')
plt.ylabel('Sepal Length in cm')
plt.show()

plt.figure(figsize=(10,6))  ## 绘制柱状图
plt.bar(range(50), iris['sepal width (cm)'][:50])
plt.title('Sepal Width Bar Chart')
plt.xlabel('Index')
plt.ylabel('Sepal Width in cm')
plt.show()

plt.figure(figsize=(10,6))  # 绘制散点图
plt.scatter(iris['sepal length (cm)'], iris['sepal width (cm)'])
plt.title('Sepal Length vs Width Scatter Plot')
plt.xlabel('Sepal Length in cm')
plt.ylabel('Sepal Width in cm')
plt.show()