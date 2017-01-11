# -*- coding: utf-8 -*-
from importer import *
utils = Utils()
db = DB()



print("Enter URL :")
site_url =raw_input().strip()
parsed_url = urlparse.urlparse(site_url)
while( not bool(parsed_url.scheme)):
        print("Enter Valid URL :")
        url =raw_input().strip()
        parsed_url = urlparse.urlparse(url)


print("Enter Element :")
element=raw_input().strip()

print("Enter Identifier :")
identifier=raw_input().strip()

print("Enter value: ")
value =raw_input().strip()


if(not site_url.endswith('/')):
        site_url = site_url+ '/'

search = {"site_url":str(site_url)}
cat_urls = catcollection.find(search)
for category in cat_urls:
	try:
		category_url = utils.createUrl(site_url,category['url'])
		page = urllib.urlopen(category_url).read()
		soup = BeautifulSoup(page)
		product_links = soup.findAll(element, {identifier : re.compile(value+'*')})
		for product_link in product_links:
			prod={}
			try:
				prod['cat_url'] = category_url
			except:
				pass
			prod['site_url'] = site_url
			product_url = utils.getVal(product_link,'href')
			product_url=utils.createUrl(site_url,product_url)
		        product_url = product_url[:product_url.rfind("?")]
			prod['product_link'] = product_url
			if(db.checkExisting(productcoll,prod)):
		                continue

			prod['fetched'] =0
			db.insert(productcoll,prod)




	except:
	     exc_type, exc_obj, exc_tb = sys.exc_info()
	     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	     print(exc_type, fname, exc_tb.tb_lineno)
	     print(sys.exc_info())
	     pass

try:
	subprocess.call("./ecom_fetch.py", shell=True)

except:
	pass
