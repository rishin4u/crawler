# -*- coding: utf-8 -*-
from importer import * 
utils = Utils()

print("Enter URL :")
url =raw_input().strip()

print("Enter Element :")
element=raw_input().strip()

print("Enter Identifier :")
identifier=raw_input().strip()

print("Enter value: ")
value =raw_input().strip()

try:
     page = urllib.urlopen(url).read()
     soup = BeautifulSoup(page)
     print(soup)	
     links = soup.findAll(element, {identifier : re.compile(value+'*')})
     for link in links:
	cat={}
	try:
		cat['url'] = url
	except:
		pass
	try:
		cat['title']= link["title"]
	except:
		pass	
	try:
		cat['href']=link["href"]
	except:
		pass
	try:
		cat['description']=link.string
	except:
		pass
	productioncoll.insert(cat)
except:
     exc_type, exc_obj, exc_tb = sys.exc_info()
     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
     print(exc_type, fname, exc_tb.tb_lineno)
     print(sys.exc_info())
     pass

