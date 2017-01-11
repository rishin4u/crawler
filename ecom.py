# -*- coding: utf-8 -*-
from importer import *
utils = Utils()
db = DB()

print("Enter URL :")
url =raw_input().strip()
parsed_url = urlparse.urlparse(url)
while( not bool(parsed_url.scheme)):
	print("Enter Valid URL :")
	url =raw_input().strip()
	parsed_url = urlparse.urlparse(url)




print("Enter Element :")
element=raw_input().strip()

while( not element):
        print("Enter Valid Element :")
	element=raw_input().strip()


print("Enter Identifier :")
identifier=raw_input().strip()
while( not identifier):
        print("Enter Valid Identifier :")
        identifier=raw_input().strip()



print("Enter value: ")
value =raw_input().strip()
while( not value):
        print("Enter Valid Value :")
        value=raw_input().strip()


if(not url.endswith('/')):
	url = url+'/'

try:
     page = urllib.urlopen(url).read()
     soup = BeautifulSoup(page)
     links = soup.findAll(element, {identifier : re.compile(value+'*')})
     for link in links:
	cat={}
	try:
		cat['site_url'] = url
	except:
		pass
	cat_url  = utils.getVal(link,'href')
        cat_url = utils.createUrl(url,cat_url)
        cat_url = cat_url[:cat_url.rfind("/")+1]
	cat['url'] = cat_url
	if(db.checkExisting(catcollection,cat)):
		continue
	cat['title'] = utils.getVal(link,'title')
	cat['description']=utils.getString(link)
	print(cat)
	catcollection.insert(cat)
except:
     exc_type, exc_obj, exc_tb = sys.exc_info()
     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
     print(exc_type, fname, exc_tb.tb_lineno)
     print(sys.exc_info())
     pass
