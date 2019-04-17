#Program Import data from Excel and plot in python used IDLE Python 3.7
#-import excel raw data to pandas data frame using pandas module
#-split columns
#- matplotlib module for scatter plot
#Before running the program in python shell, it is required to install pandas, xlrd and matplotlib module in Anaconda prompt.
#Commands are:
#>>cd\
#>> python –m pip install pandas
#>> python –m pip install xlrd
#>> python –m pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel (r'C:\Users\saurav\Desktop\work2.xlsx') 
df1 = df.iloc[:,0:1]
df2 = df.iloc[:,1:2]
print('Extracted from excel')
print(df)
print('First column')
print(df1)
print('Second column')
print(df2)
plt.scatter(df1,df2)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('y vs. x plot')
plt.legend('plot')
plt.show()

