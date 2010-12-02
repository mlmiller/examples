from couchdbkit import Server, Database
import sys, os, random

def safeRecord(db, doc):
  if db.doc_exist(doc['_id']):
    doc['_rev'] = db.get_rev(doc['_id'])
  db.save_doc(doc)

if __name__=='__main__':
  uri = sys.argv[1]
  cloudant = Server(uri)
  db = cloudant.get_or_create_db('seo2')
  
  ndays = 1
  years = [2010]
  months = [11,12]
  days = range(30)
  
  #urls for pages
  urls = []
  for i in range(0,10):
    urls.append('http://www.page%i.com' % i)
    
  #urls for links embedded in pages
  links = []
  for i in range(0,5):
    links.append('http://www.link%i.com' % i)

  #first make some documents
  for year in years:
    for month in months:
      for day in days:        
        print 'upload: %i/%i/%i' % (year,month, day)
        for url in urls:
          #hack because I was too lazy to lookup urlparsing in python
          base = url.split('.')[1]
          
          doc = {'_id':'%s_%i_%i_%i' % (base, year, month, day)}
          doc['date'] = [year, month, day]
          doc['url'] = url
          doc['links'] = []
          
          #and choose whether or not to add the links
          for link in links:
            if random.random()>0.5: #keep it
              doc['links'].append(link)
              
        safeRecord(db, doc)
  