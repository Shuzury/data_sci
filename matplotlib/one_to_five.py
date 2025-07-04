## importing matplotlib
'''  ## demo tha niche 
import matplotlib.pyplot as plt
x=[1,2,3,4] #horizontal axis
y=[10,20,15,20] #vertical axis

plt.plot(x,y)
plt.show()
'''
'''import matplotlib.pyplot as plt
x = [ 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
y=[37,20,15,27,25,30,35] 
plt.plot(x,y)
plt.title('Saptahik Bikri Data')
plt.xlabel('Din')
plt.ylabel('Bikri (in units)')
plt.show()'''

## matplotlib OOA- object oriented api
# # data visualisation using matplotlib
# # Matplot plotting functions ->grid,show,axis limits, axis ticks,legends,titles,plot,labels,colors,markers,linestyles ->heyi chatgpt , do write about them like functions and example codes etc

import matplotlib.pyplot as plt

# Define data
x = [ 1,2,3,4,5,6,7,9,10,11,12]  
y=[37,20,15,27,25,30,35,40,5,50,67]  
plt.plot(x, y, label='Cakes bikri', linewidth=2, marker='o', color='green', linestyle='--') # heyi chatgpt , explain each
plt.title('Bikri Data')
plt.xlabel('Mahine') # x axis ka naam
plt.ylabel('Bikri (in units)')
plt.legend(loc='lower right') # woh jo "label= 'Cakes bikri'" diya hai, wahi dikhane ke liye "lagend()" use hota hai
plt.grid(color='purple', linestyle=':', linewidth=1) # heyo chatgpt, explain this
plt.ylim(0, 80)  # Set y-axis limits, s axis ka bhi same for numbers only , not words or strings
# plt.show()
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
# heyi chatgpt, explain this xtick
plt.yticks([0, 20, 40, 60, 80], ['Zero', 'Low', 'Medium', 'High', 'Very High'])
'''NOTE - disable xtick and y tick to see as "quanity vs week number" graph'''
plt.show()
# heyi chatgpt , do show for both with and without x ticks and y ticks
