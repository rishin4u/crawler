class DB():


    def insert(self,collection,object):
        try:
		if(collection.insert(object)):
			return 1
		else:
			return 0 
	except:
		return 0

    def get(self,collection,object):
	try:
		return collection.find(object)
	except:
		return None

    def update(self,collection,search,update) :
	try:	
		updateobj = {'$set':update}
		if(collection.update(search,updateobj)):
			return 1
		else:
			return 0 
	except:
		return 0 
	
    def checkExisting(self,collection,search):
	try:
                return collection.count(search)
        except:
                return 0

