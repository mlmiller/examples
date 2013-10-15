from multiprocessing import Pool
from pyItunes import *
import restkit
import sys
import os
import time
import ConfigParser
import requests
from multiprocessing import Pool
import json

def get_creds(f=os.path.expandvars('$HOME/.clou')):
	config = ConfigParser.ConfigParser()
	config.read(f)
	return {'user':config.get('cloudant','user'), 'pwd':config.get('cloudant','password')}

def makeDoc(song):
	doc = song.__dict__
	doc['date_added'] = int(time.mktime(doc['date_added']))
	doc['date_modified'] = int(time.mktime(doc['date_modified']))
	return doc

if __name__=="__main__":

	#grab the itunes data and parse it
	lib = Library(XMLLibraryParser(sys.argv[1]).dictionary)
	docs = [makeDoc(song) for song in lib.songs]

	#where to stick it
	creds = get_creds()
	headers = {'Content-type': 'application/json'}
	auth = (creds['user'], creds['pwd'])
	uri = 'https://%s.cloudant.com/it_1' % (creds['user'])

	#save data
	pool = Pool(processes=10)
	pool.map(requests.post(uri, auth=auth, data=json.dumps(doc), headers=headers), docs)

