'''charts and histograms'''
# (Bar, histogram, pie) charts- Hey chatgpt, explain them with need and problems for matplotlib based on code below
import matplotlib.pyplot as plt
x = [' A', ' B', ' C', ' D']
y = [150, 230, 120, 310]
# Bar chart
# plt.bar(x, y, color='skyblue',width= val, label='Sales Data') # syntax
plt.bar(x, y, color='Red' , label='Sales Data')  
plt.title('Sale ki tulna')  
plt.xlabel('Maal')  
plt.ylabel('Bikri')
plt.legend(loc='upper left')  
plt.show()  # Display the bar chart