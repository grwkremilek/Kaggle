import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.DataFrame()             #convert a Python object (dictionary, lists etc) to pandas df
df.to_filetype(filename)        #save a df to a file

##INSPECTING DATA
df.head(n)
df.tail(n)
df.shape                        #show the number of rows and columns
df.info()                       #show the index, datatype and memory information
df.describe()                   #summary statistics for numerical columns

s.value_counts(dropna=False)
df.mean()                       #return the mean of all columns
df.corr()                       #return the correlation between columns in a data frame
df.count()                      #return the number of non-null values in each data frame column
df.max()                        #return the highest value in each column
df.min()                        #return the lowest value in each column
df.median()                     #return the median of each column
df.std()                        #return the standard deviation of each column

##SELECTING DATA
df[col]                         #return column with label col as Series
df[[col1, col2]]                #return columns as a new DataFrame
s.iloc[0]                       #select by position
s.loc['index_one']              #select by index
df.iloc[0,:]                    #select the first row
df.iloc[0,0]                    #select the first element of the first column

#FILTER, SORT, GROUPBY
df[df[year] > 1984]             # boolean filtering, use & (and) or | (or) to add different conditions
df.sort_values(col1)            # sort values in an ascending order
df.sort_values(col2,ascending=False) # sort values in an descending order
df.sort_values([col1,col2],ascending=[True,False])
df.groupby(col)                 #return a groupby object for values from one column
df.groupby([col1,col2])         #returns a groupby object for values from multiple columns

#MISSING VALUES
pd.isnull()                     #return a boolean array (an array of true for missing values and false for non-missing values)
pd.isnull().sum()               #get a sum of null/missing values
pd.notnull()                    #return the opposite of isnull()
df.dropna()                     #drop missing values in the rows
df.dropna(axis=1)               #drop missing values in the columns
df.fillna(x)                    #fill the missing values with other values

#REPLACE
s.replace(1,'one')              #replace 1 for 'one'
s.replace([1,3],['one','three'])#replace more values

#RENAME
df.rename(columns={'old_name': 'new_ name'})
df.set_index('column_one')      #change the index of the data frame


#JOIN/COMBINE
df1.append(df2)                 #add the rows in df1 to the end of df2 (columns should be identical)
pd.concat([df1, df2],axis=1)    #add the columns in df1 to the end of df2 (rows should be identical)
df1.join(df2,on=col1,how='inner')#SQL-style join the columns in df1 with the columns on df2 where the rows for colhave identical values
