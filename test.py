import pandas as pd

ReactionTypes = r"data/ReactionTypes.csv"
Reactions = r"data/Reactions.csv"
Content = r"data/Content.csv"

# Load and clean Content data
ReactionTypes_data = pd.read_csv(ReactionTypes)
Reactions_data=pd.read_csv(Reactions)
Content_data=pd.read_csv(Content)

# Drop unwanted data
Content_data=Content_data.drop(columns="URL",axis=1)
Content_data=Content_data.drop(columns="User ID",axis=1)

# Clean and Organize Data
Content_data["Category"] = Content_data["Category"].str.replace('"', '')
Content_data=Content_data.rename(columns={'Type':"Content Type"})

# file_path= r"Output Data1.xlsx"
# Content_data.to_csv(file_path,index=False)
# print(f"Excel file saved to {file_path}")

# Drop Unwanted and null data
Reactions_data=Reactions_data.drop(columns="User ID",axis=1)
Reactions_data = Reactions_data.dropna()

# file_path= r"Output Data2.xlsx"
# Reactions_data.to_csv(file_path,index=False)
# print(f"Excel file saved to {file_path}")

# Merge Content and Reactions data on "Content ID"
data1=Reactions_data
data2=Content_data
data=pd.merge(data1,data2,on="Content ID",how='left', suffixes=('_data1', '_data2'))
data=data.drop(columns="Unnamed: 0_data2",axis=1)

# file_path= r"Output Data3.xlsx"
# data.to_csv(file_path,index=False)
# print(f"Excel file saved to {file_path}")

# Merge with ReactionTypes data on "Type"
data3=data
data4=ReactionTypes_data
Clean_data=pd.merge(data3,data4,on="Type",how='left', suffixes=('_data3', '_data4'))
Clean_data=Clean_data.drop(columns="Unnamed: 0",axis=1)

# Save the final cleaned dataset to Excel
file_path= r"A cleaned dataset.xlsx"
Clean_data.to_csv(file_path,index=False)
print(f"Excel file saved to {file_path}")

# rename the similar categeroris
Clean_data["Category"]=Clean_data["Category"].str.replace("animals","Animals")
Clean_data["Category"]=Clean_data["Category"].str.replace("healthy eating","Healthy Eating")
Clean_data["Category"]=Clean_data["Category"].str.replace("technology","Technology")
Clean_data["Category"]=Clean_data["Category"].str.replace("science","Science")
Clean_data["Category"]=Clean_data["Category"].str.replace("culture","Culture")
Clean_data["Category"]=Clean_data["Category"].str.replace("travel","Travel")
Clean_data["Category"]=Clean_data["Category"].str.replace("food","Food")
Clean_data["Category"]=Clean_data["Category"].str.replace("education","Education")
Clean_data["Category"]=Clean_data["Category"].str.replace("soccer","Soccer")
Clean_data["Category"]=Clean_data["Category"].str.replace("fitness","Fitness")
Clean_data["Category"]=Clean_data["Category"].str.replace("public speaking","Public Speaking")
Clean_data["Category"]=Clean_data["Category"].str.replace("veganism","Veganism")
Clean_data["Category"]=Clean_data["Category"].str.replace("studying","Studying")

#top 5 Categories
category_counts = Clean_data['Category'].value_counts()
print("Top 5 Categories")
print(category_counts.head(5))


# top 5 Reaction
top_reactions = Clean_data['Type'].value_counts()
print("Top 5 Reaction Type")
print(top_reactions.head(5))