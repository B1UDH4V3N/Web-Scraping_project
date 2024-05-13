from WebScrap_1 import *
from DateTime_3 import *
from Excel_2 import *
from mail_6 import *
import pandas as pd
import visualization_7
def track():
    fp=open("Flipkart_Dataset.csv","a+", newline='', encoding='utf-8')
    writer=csv.writer(fp)
    writer.writerow(data)
    fp.close()
    if int(pr1) < 65000:
        mail()

    df=pd.read_csv('Flipkart_Dataset.csv')
    visualization_7.visualize_price_trend(df)


while(True):
    track()
    time.sleep(86400)
    