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

# Scatter Plot -> to find corln between two variables
#plt.scatter(x, y, color='color', marker='marker_style', label='label') #syntax
# import matplotlib.pyplot as plt
# hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# exam_scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# plt.scatter(hours_studied, exam_scores, color='orange', marker='o', label='chatra ka data')
# plt.xlabel('Padne ke ghante')
# plt.ylabel('exam ke marks')
# plt.title('Padne ke ghante aur exam ke marks ka relation')
# plt.legend(loc='upper left')
# plt.grid(True)  
# plt.show()  
'''import matplotlib.pyplot as plt
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores_A = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# Another class for comparison
exam_scores_B = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]  
plt.scatter(hours_studied, exam_scores_A, color='orange', marker='o', label='Class A')
# Adding another class for comparison
plt.scatter(hours_studied, exam_scores_B, color='blue', marker='s', label='Class B')  
plt.xlabel('Padne ke ghante')
plt.ylabel('exam ke marks')
plt.title('Padne ke ghante aur exam ke marks ka relation')
plt.legend(loc='upper left')
plt.grid(True)  
plt.show()  '''

'''Note heyi chatgpt explain the different types of markers available in matplotlib for scatter plots, like 'o', 's', '^', etc.'''
# Scatter Plot -> to find correlation between temperature and ice cream sales
# import matplotlib.pyplot as plt
# temperature = [20, 22, 25, 27, 30, 32, 35, 37, 40, 42]
# ice_cream_sales = [100, 120, 150, 170, 200, 220, 260, 280, 320, 350]
# plt.scatter(temperature, ice_cream_sales, color='blue', marker='^', label='Sales Data')
# plt.xlabel('Temperature (°C)')
# plt.ylabel('Ice Cream Sales')
# plt.title('Temperature vs Ice Cream Sales')
# plt.legend(loc='upper left')
# plt.grid(True)
# plt.show()


# subplot and layout adjustment
'''
import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5, 6, 7]
y=[10,20,15,25,37,7,31]

plt.subplot(2, 2, 1)  # 2 rows, 2 columns, first graph
plt.plot(x, y, color='blue', marker='o')
plt.title('Line Chart')

plt.subplot(2, 2, 2)  # 2 rows, 2 columns, second graph
plt.bar(x, y, color='blue')
plt.title('Bar Chart')
# plt.tight_layout()  # basically pura page ka space utilize karta hai, so that graphs are not overlapping
plt.tight_layout()  # hey chatgpt , please explan this 
plt.show()
'''

'''
import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5, 6, 7]
y=[10,20,15,25,37,7,31]

# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5)) #syntax
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Line plot
ax[0].plot(x, y, color='blue')
ax[0].set_title('Line Plot')

# Bar chart
ax[1].bar(x, y, color='green')
ax[1].set_title('Bar Chart')
plt.tight_layout()
fig.suptitle('Bar evang line chart ka comparision')  # Add a title for the entire figure
plt.show()
'''
# # NOTE hey chatgpt, please explain the difference between the last 3 codes i.e the one with "fig,ax" and the one wihout

'''savefig'''
## basically generated charts ya graph ya figures ko save karta hai to present or display or use later
##png,svg,pdf etc. format mey save karta hai
## syntax: plt.savefig('filename.format', dpi=value, bbox_inches='tight') #dpi generally 300 for good quality, bbox = tight matlab as pass no blank white space
'''
import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5, 6, 7]
y=[10,20,15,25,37,7,31]
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax[0].plot(x, y, color='blue')
ax[0].set_title('Line Plot')
ax[1].bar(x, y, color='green')
ax[1].set_title('Bar Chart')
plt.tight_layout()
fig.suptitle('Bar evang line chart ka comparision')  # Add a title for the entire figure
plt.savefig('chart_comparison.png', dpi=300, bbox_inches='tight')  
plt.show()
'''
## NOTE file bahar wale folder i.e DATA_SCI mey store hua hai
## to save in a specified folder 
import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5, 6, 7]
y=[10,20,15,25,37,7,31]
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax[0].plot(x, y, color='blue')
ax[0].set_title('Line Plot')
ax[1].bar(x, y, color='green')
ax[1].set_title('Bar Chart')
plt.tight_layout()
fig.suptitle('Bar evang line chart ka comparision')  # Add a title for the entire figure
plt.savefig('matplotlib\compare.png', dpi=300, bbox_inches='tight')  #check terminal , waha sey continue karna path , naki from c:. . .
plt.show()