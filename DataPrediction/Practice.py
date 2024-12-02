import pandas as pd
df = pd.read_csv("coffee_survey.csv")
df.head()

rows=len(df.axes[0])
cols=len(df.axes[1])

print("Rows : ",rows)
print("Columns : ",cols)
result=df.head(10)
print("First 10 rows")
print(result)
dataTypes=df.dtypes
print("data types of each columns")
print(dataTypes)
# NullVal=df.isnull
# print("Printing null values :",NullVal)
print("\n")
missing_data=df.isnull().sum()

missing_columns=missing_data[missing_data>0]
print("missing data and there count : ")
print(missing_columns)

print("\n")

threshold=0.2
#calculate the percentage of missing values
missing_percentage=df.isnull().mean()

#identify columns with more than 20% missing values
columns_to_handle=missing_percentage[missing_percentage > threshold].index
print("Columns with more than 20% missing values : ",columns_to_handle.to_list())

#Summary for statistics
summary_stats={}
for column in df.select_dtypes(include=['float64','int64']).columns:
    summary_stats[column]={
        'mean':df[column].mean(),
        'median':df[column].median(),
        'mode':df[column].mode().tolist(),
        'std_dev':df[column].std(),
        'min': df[column].min(),
        'max': df[column].max(),
        'count': df[column].count()
    }
#Convert summary into dataframe
summary_df=pd.DataFrame(summary_stats).T

print("Summary Statistics:")
print(summary_df)