import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver")
browser.get(start_url)


time.sleep(10)

#headers = ["Proper name", "Distance", "Mass", "Radius","Luminosity"]
Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

def Scrape():

    
    soup = BeautifulSoup(browser.page_source, "html.parser")

    temp_list = []
    for tr_tag in soup.find_all("tr"):
        td = tr_tag.find_all("td")
        row = []
        
        for i in td:
            row.append(i.text.rstrip())
        temp_list.append(row)   
       
        #for index,td_tags in enumerate(td):
            
            #if index == 1 :
                #if td_tags.find("a"):
                    #temp_list.append(td_tags.find("a").contents[0])     
                    
            #else:

                #try:
                    #temp_list.append(td_tags.contents[0])

                #except:
                    #temp_list.append("")
                #planet_data.append(temp_list)
                
    for i in range(1,len(temp_list)):
        Star_names.append(temp_list[i][1])
        Distance.append(temp_list[i][3])
        Mass.append(temp_list[i][5])
        Radius.append(temp_list[i][6])
        Lum.append(temp_list[i][7])

Scrape()

  
df = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df)

df.to_csv('Scraper.csv')

#with open("Scraper.csv", "w") as f:
    #writer = csv.writer(f)
    #writer.writerow(headers)
    #writer.writerows(planet_data)




