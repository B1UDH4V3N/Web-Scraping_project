import csv
from WebScrap_1 import *
from DateTime_3 import *
header= ['Title','Price(₹)','Rating','Date']
data=[title1,pr1,rating1,today]

#write csv file

# fp=open("Flipkart_Dataset.csv","w", newline='', encoding='utf-8')       #Avoid unicode error (maybe insert special symbol)
# '''fp.writerow(header)
# fp.writerow(data)
# fp.close()  '''                              #This gives error as writerow() method belongs to the csv.writer object, not the file object itself.
# writer=csv.writer(fp)
# writer.writerow(header)
# writer.writerow(data)
# fp.close()
#----------------------------------------------------------------------------------------------
#inserting (append) data to file
'''fp=open("Flipkart_Dataset.csv","a+", newline='', encoding='utf-8')
writer=csv.writer(fp)
writer.writerow(data)
fp.close()'''

#copy this code in final tracker......