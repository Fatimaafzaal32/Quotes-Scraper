import requests,time,csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url='https://quotes.toscrape.com/'
try:
    r=requests.get(url,timeout=10)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
   print('Request Fail',e)
   exit()

  
list1=[]
seen=set()
while True:
   
   soup=BeautifulSoup(r.text,'html.parser')
   quotes=soup.find_all('div',class_='quote')
   for quote in quotes:
        span=quote.find('span',class_='text')
        if span:
          
           Quotes=span.text.strip()
        else:
           Quotes=''
        small=quote.find('small',class_='author')
        if small:
          
           Authors=small.text.strip()
        else:
           Authors=''
        tags=quote.find('div',class_='tags')
        if tags:

          Tags = [tag.text.strip() for tag in tags.find_all('a', class_='tag')]
          Tags = ', '.join(Tags)
        else:
         Tags=''
        dictionary={
             'Quotes':Quotes,
             'Authors':Authors,
             'Tags':Tags
             }
        unique_values=(Quotes)
        if unique_values not in seen:
           seen.add(unique_values)
           list1.append(dictionary)

   next=soup.find('li',class_='next')
   if next is None:
      break
   nexturl=next.find('a').get('href')
   next_url=urljoin(url,nexturl)
   url=next_url
   time.sleep(1)
   try:
      r=requests.get(url,timeout=10)
      r.raise_for_status()
   except requests.exceptions.RequestException as e:
      print("rquest failed" ,e)
      break
with open('Quotes.csv','w',newline='',encoding='utf-8') as file:
   writer=csv.DictWriter(file,fieldnames=['Quotes','Authors','Tags'])
   writer.writeheader()
   writer.writerows(list1)
print(f"Total quotes scraped: {len(list1)}")
      

   

    
    
    

    

        
 