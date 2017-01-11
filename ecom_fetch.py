from importer import *
utils = Utils()
db = DB()

search = {"fetched":0}
results = db.get(productcoll,search)

for product in results:
	product_link = utils.getVal(product,'product_link')
	page = urllib.urlopen(product_link).read()
	soup = BeautifulSoup(page)
     	title = soup.find("h1")
	try:
		title = re.sub('<[^<]+?>', '', str(title))
		update ={"title":title,"fetched":1}
		db.update(productcoll,product,update)
		print(title)
 	except:
		exc_type, exc_obj, exc_tb = sys.exc_info()
	        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
     		print(exc_type, fname, exc_tb.tb_lineno)
     		print(sys.exc_info())
     		pass


