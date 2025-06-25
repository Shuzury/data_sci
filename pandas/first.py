# # ISME HUM SKHENGE HOW TO READ DIFFERENT FILES
# import pandas as pd
# # # to read a csv file
# # df=pd.read_csv("pract\sales_data_sample.csv",encoding="latin1") #df= var name for DATAFRAME

# # # to read excel file
# # df = pd.read_excel("pract\SampleSuperstore.xlsx")

# # # to read json file
# df=pd.read_json("pract\sample_Data.json")
# print(df)




# # # here we will learn how to Create,save files etc after work
# import pandas as pd

# data = {
#     "Name":['Shaunak','Sarthak','Ronit'],
#     "Age":[10,20,30],
#     "City":['Shillong','Silchar','Hailakandi']
# }
# # #creating Dataframe
# df=pd.DataFrame(data)
# print(df)

# # #Saving the file in csv
# # # df.to_format("path\filename.format",index=your_choice)-> if idnex=false,serial no removed , else serial no. rehta hai
# # df.to_csv("pract\pratham.csv",index=False)
# # write the code for xlsx and json too

