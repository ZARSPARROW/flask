#pip install flask
#pip install pandas
#using custombusiness day , pd.date_range,date-format, pd.dataframe, pd.concat, .tolist()
#python for loop if 

import pandas as pd
from datetime import date
#from pandas.tseries.offsets import Day
from pandas.tseries.holiday import *
from pandas.tseries.offsets import CustomBusinessDay


class myCalendar(AbstractHolidayCalendar):
   rules = [
     Holiday("New Years Day", month=1, day=1, observance=nearest_workday),
     Holiday("New Years Day", month=1, day=2, observance=nearest_workday),
     Holiday("New Years Day", month=1, day=3, observance=nearest_workday),
     Holiday("New Years Day", month=1, day=4, observance=nearest_workday),
     Holiday("New Years Day", month=5, day=3, observance=nearest_workday),
     Holiday("New Years Day", month=5, day=6, observance=nearest_workday),
     Holiday("Independence Day", month=7, day=15, observance=nearest_workday),
     Holiday("Veterans Day", month=8, day=14, observance=nearest_workday),
     Holiday("New Years Day", month=8, day=15, observance=nearest_workday),
     Holiday("New Years Day", month=8, day=16, observance=nearest_workday),
     Holiday("'体育の日", month=10, day=14, observance=nearest_workday),
     Holiday("New Years Day", month=12, day=30, observance=nearest_workday),
     Holiday("Black Friday", month=12, day=31, observance=nearest_workday),

   ]
# umc-workingday #
#using CustomBusinessDay
cal = CustomBusinessDay(calendar=myCalendar())
#start to end frequency with calling custombusinessday
s = pd.date_range('2019-01-01', '2019-12-31' , freq=cal)
#date format 
sumc=s.strftime('%Y-%m-%d')
#extra date (saturday and sunday )
s1 =['2019-12-28']
#Calling DataFrame constructor on s
df = pd.DataFrame(sumc,columns=['umc'])
#Calling DataFrame constructor on s1
df1 = pd.DataFrame(s1,columns=['umc'])
#concatenating df and df1 on  Dataframe
data= pd.concat([df,df1], ignore_index=True)
# converting to list 
umcdata = {'umc-workingday' : data["umc"].tolist()}
def umc():
  return umcdata

# umc-holiday #
# converting to list 
umc=data["umc"].tolist()
#start to end frequency
s = pd.date_range(start='2019-01-01',end='2019-12-31' )
#date format
Allday=s.strftime('%Y-%m-%d')
#Calling Dataframe constructor on Allday
df = pd.DataFrame(Allday, columns=['umc'])
#converting to list
Calendar=df["umc"].tolist()
#python for loop and if condition
holiday={'umc-holiday':[date for date in Calendar if not date in umc]}
def umchol():
    return holiday


# uvi #
s = pd.date_range('2019-01-01', '2019-12-31' , freq=cal)
sumc=s.strftime('%Y-%m-%d')
s1 =['2019-12-28']
df = pd.DataFrame(sumc,columns=['umc'])
df1 = pd.DataFrame(s1,columns=['umc'])
data= pd.concat([df,df1], ignore_index=True)
uvidata = {'uvi-workingday' : data["umc"].values.tolist()}
def uvi():
      return uvidata 
      
#create json file
#with open('./population.json', 'w') as f:
    #json.dump(data, f, ensure_ascii=False)
 


