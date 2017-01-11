class Utils():


    def getVal(self,obj,key):
        try:
		return obj[key]
	except:
		return None

    def getString(self,obj):
	try:
		return obj.string
	except:
		return None

    def createUrl(self,url,link):
        try:
            	if(link.startswith(("http://","https://"))):
                	return link
            	else:
                	return url+link.lstrip('/')

        except:
            return None
