'''charts and histograms'''
# (Bar, histogram, pie) charts- Hey chatgpt, explain them with need and problems for matplotlib based on code below
'''
# Bar chart
# plt.bar(x, y, color='skyblue',width= val, label='Sales Data') # syntax
import matplotlib.pyplot as plt
x = [' A', ' B', ' C', ' D']
y = [150, 230, 120, 310]
plt.bar(x, y, color='Red' , label='Sales Data')  
# plt.barh(x, y, color='Red' , label='Sales Data')  # add 'h' after  "bar" for horizontal bar chart
plt.title('Sale ki tulna')  
plt.xlabel('Maal')  
plt.ylabel('Bikri')
plt.legend(loc='upper left')  
plt.show()  # Display the bar chart
'''

'''
# pie chart -> total ko tukro mey batta hai  so that kisne kitna contribute kiya hai
import matplotlib.pyplot as plt
# plt.pie(values, labels=labels,colours=[colour_list] autopct='%1.1f%%') # syntax:
# hey chatgpt , please explain "%1.1f%%" in the above syntax
x=['North', 'South', 'East', 'West']
y=[3000,1500,7000,2000]
plt.pie(y, labels=x, colors=['gold', 'skyblue', 'lightgreen', 'coral'], autopct='%1.1f%%')  
plt.title("Bikri region anusar")
plt.show()
'''

'''
# Histogram ->hey chatgpt , upar bakio ke jaisa iska bhi description likh dena
import matplotlib.pyplot as plt
# plt.hist(data, bins=number_of_bins, color='color', edgecolor='edge_color') # syntax
scores = [30, 42, 43, 44, 45, 46, 47, 48, 49, 50, 77, 85, 88, 91, 94, 97, 99, 99, 97, 99, 67, 94]
plt.hist(scores, bins=5, color='purple', edgecolor='black')  
plt.xlabel('Scores Range')
plt.ylabel('Score distribution')
plt.title("Score ka vitran")
plt.show()  
'''

# Scatter Plot