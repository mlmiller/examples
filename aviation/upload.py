from couchdbkit import Server
from couchdbkit.loaders import FileSystemDocsLoader
from csv import DictReader
import time, sys, gzip

def upload(db, reader, checkpoint = 1000):
  docs = list()
  ndocs = 0
  start = time.time()

  for doc in reader:
    ndocs += 1
    docs.append(doc)
    # print doc
    if (len(docs) % checkpoint == 0):
      print 'upload:\t%i' % ndocs
      db.bulk_save(docs)
      del docs
      docs = list()

  # don't forget the last batch
  db.bulk_save(docs)

  #print summary statistics
  delta = time.time() - start
  rate = float(checkpoint) / float(delta)
  print 'uploaded: %i docs in: %i seconds for a rate: %f docs/sec' % (ndocs, delta, rate)

if __name__=='__main__':

  fname = sys.argv[1]
  uri = sys.argv[2]
  dbname = sys.argv[3]

  print 'Upload contents of %s to %s/%s' % (fname, uri, dbname)

  # #connect to the db
  cloudant = Server(uri)
  db = cloudant.get_or_create_db(dbname)
  print db.info()

  #sync the views for prebuilt indices
  loader = FileSystemDocsLoader('_design/')
  loader.sync(db, verbose=True)

  #loop on file for upload
  try:
    reader = DictReader(gzip.open(fname, 'rb'), delimiter = '|')
    upload(db, reader)
  except IOError:
    reader = DictReader(open(fname), delimiter = '|')
    upload(db, reader)

