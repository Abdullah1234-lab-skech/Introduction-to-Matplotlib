import matplotlib.pyplot as plt
import numpy as np
categories = ['A', 'B', 'C', 'D']                   
values = [23, 45, 56, 78]
x = np.arange(len(categories))
plt.bar(x , values , color='blue', width=0.4)
plt.xticks(x, categories)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart of Categories vs Values')
plt.show()