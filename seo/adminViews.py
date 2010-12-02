from couchdbkit.loaders import FileSystemDocsLoader
from couchdbkit import Server, Database
import sys, os


path_to_design = sys.argv[1]
uri = sys.argv[2]
dbname = sys.argv[3]
print 'upload views from directory root:\t%s \t to db:\t%s/%s' % (path_to_design, uri,dbname)
server = Server(uri)
db = server.get_or_create_db(dbname)

loader = FileSystemDocsLoader(path_to_design)
loader.sync(db, verbose=True)
