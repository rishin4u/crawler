import os, sys,urllib2,json,urllib,time
lib_path = os.path.abspath('/var/www/ecom/lib/beautifulsoup4-4.1.2')
sys.path.append(lib_path)
from pymongo import MongoClient as Connection
from urlparse import urlparse
from bson import BSON
from bs4 import BeautifulSoup
from utils import Utils
import re,urlparse,subprocess
from db import DB
connection = Connection()
db = connection.ecom
catcollection = db.ecomcat
productcoll = db.ecomprod
