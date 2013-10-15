# Data Modeling and Relational Analysis in a NoSQL World 

	Mike Miller (Cloudant)
	Last Modified: 10/14/2013
	
You can play along at home with this example by performing the following steps:

## Get a free Cloudant account.  
Head to [http://cloudant.com](http://cloudant.com) and sign up for an account on the Malort cluster (Rackspace-Chicago).

## Manage replications
Create a `_replicator` database to manage your replication between databases.  You can do this by navigating to [your user dashboard on cloudant.com](https://cloudant.com/dashboard/#!/dashboard) or performing the simple command below from a shell/terminal.
	
	curl -X PUT -u username 'https://username.cloudant.com/_replicator'
	
## Replicate the demo data
To trigger a replication we follow the instructions from the [CouchDB documentation](http://wiki.apache.org/couchdb/Replication#Replicator_database).  We encapsulate information about the source and target databases into a single document.  Then navigate to the cloudant.com dashboard and create a new document.  Choose "View Source" and past the following into the form:

		{
		    "source": "https://malortmike.cloudant.com/itunes1",
		    "target": "https://username:pwd@username.cloudant.com/itunes1",
			"worker_processes": 20,
			"worker_batch_size": 500,
			"http_connections": 500,
			"create_target": true,
			"connection_timeout": 60000
		}
After saving the document, the replication should start and finish in a matter of seconds.

## Validating the replication
After the replication is complete, you should be able to perform the following check:

	curl -u username 'https://username.cloudant.com/itunes1'

and receive a response like:

	{
	  "instance_start_time": "0",
	  "compact_running": false,
	  "update_seq": "8112-g1AAAADjeJzLYWBgYMlgTmGQSUlKzi9KdUhJMtTLTU1M0UvOyS9NScwr0ctLLckBqmJKZEiy____f1YSAwPHQuK0JDkAyaR6qC7W6cTpymMBkgwNQAqocT_Yvj2k6DwA0Qlx6Z4sAPsySRs",
	  "db_name": "itunes1",
	  "purge_seq": 0,
	  "other": {
	    "data_size": 4960860
	  },
	  "doc_del_count": 0,
	  "doc_count": 8112,
	  "disk_size": 6320548,
	  "disk_format_version": 5
	}
	
## Test with a query
You should be able to then perform a query like the following:

	curl -g -u 'username' 'https://username.cloudant.com/itunes1/_design/ana1/_search/simple_search?q=artist:diplo&sort=["play_count"]' | jq '.'

and receive a response like:
	
	{
	  "rows": [
	    {
	      "fields": {
	        "bit_rate": 256,
	        "date_modified": 1255589696,
	        "year": 2008,
	        "sample_rate": 44100,
	        "size": 10329612,
	        "location": "file://localhost/Users/mlmiller/Music/iTunes/iTunes%20Media/Music/Diplo/Blow%20Your%20Head%20-%20EP/03%20Wassup%20Wassup%20(feat.%20Rye%20Rye)%20%5BCrookers%20Remix%5D.m4a",
	        "genre": "Hip-Hop/Rap",
	        "total_time": "298939",
	        "name": "Wassup Wassup (feat. Rye Rye) [Crookers Remix]",
	        "play_count": 5,
	        "artist": "Diplo",
	        "track_number": "3",
	        "compilation": "false",
	        "date_added": 1330301103,
	        "album": "Blow Your Head - EP",
	        "album_artist": "Diplo",
	        "kind": "Purchased AAC audio file"
	      },
	      "order": [
	        5,
	        1712
	      ],
	      "id": "af46ba14ca9de81e3e86f1bdf0bfccec"
	    },
	    {
	      "fields": {
	        "bit_rate": 256,
	        "kind": "Purchased AAC audio file",
	        "year": 2012,
	        "composer": "Diplo, Billy the Gent &#38; Long Jawns",
	        "sample_rate": 44100,
	        "size": 9956710,
	        "location": "file://localhost/Users/mlmiller/Music/iTunes/iTunes%20Media/Music/Diplo/Express%20Yourself%20-%20EP/05%20Butters%20Theme%20(feat.%20Billy%20the%20Gent%20&#38;%20Long%20Jawns).m4a",
	        "genre": "Dance",
	        "total_time": "266666",
	        "name": "Butters Theme (feat. Billy the Gent &#38; Long Jawns)",
	        "date_modified": 1339608770,
	        "play_count": 13,
	        "artist": "Diplo",
	        "track_number": "5",
	        "compilation": "false",
	        "date_added": 1339608758,
	        "album": "Express Yourself - EP",
	        "album_artist": "Diplo"
	      },
	      "order": [
	        13,
	        1582
	      ],
	      "id": "1adbc6c55edfa143275ff2a781f8550c"
	    },
	    {
	      "fields": {
	        "bit_rate": 256,
	        "kind": "Purchased AAC audio file",
	        "year": 2012,
	        "composer": "Diplo &#38; Lazerdisk Party Sex",
	        "sample_rate": 44100,
	        "size": 8608086,
	        "location": "file://localhost/Users/mlmiller/Music/iTunes/iTunes%20Media/Music/Diplo/Express%20Yourself%20-%20EP/06%20Set%20It%20Off%20(feat%20Lazerdisk%20Party%20Sex).m4a",
	        "genre": "Dance",
	        "total_time": "240000",
	        "name": "Set It Off (feat Lazerdisk Party Sex)",
	        "date_modified": 1339608771,
	        "play_count": 13,
	        "artist": "Diplo",
	        "track_number": "6",
	        "compilation": "false",
	        "date_added": 1339608758,
	        "album": "Express Yourself - EP",
	        "album_artist": "Diplo"
	      },
	      "order": [
	        13,
	        1729
	      ],
	      "id": "1adbc6c55edfa143275ff2a781f88305"
	    },
	    {
	      "fields": {
	        "bit_rate": 256,
	        "kind": "Purchased AAC audio file",
	        "year": 2012,
	        "composer": "Diplo &#38; GTA",
	        "sample_rate": 44100,
	        "size": 6982603,
	        "location": "file://localhost/Users/mlmiller/Music/iTunes/iTunes%20Media/Music/Diplo/Express%20Yourself%20-%20EP/04%204.%20Move%20Around%20(feat.%20Elephant%20Man%20&#38;%20GTA).m4a",
	        "genre": "Dance",
	        "total_time": "194187",
	        "name": "4. Move Around (feat. Elephant Man &#38; GTA)",
	        "date_modified": 1339608767,
	        "play_count": 14,
	        "artist": "Diplo",
	        "track_number": "4",
	        "compilation": "false",
	        "date_added": 1339608758,
	        "album": "Express Yourself - EP",
	        "album_artist": "Diplo"
	      },
	      "order": [
	        14,
	        1583
	      ],
	      "id": "1adbc6c55edfa143275ff2a781f85a81"
	    },
	    {
	      "fields": {
	        "bit_rate": 256,
	        "kind": "Purchased AAC audio file",
	        "year": 2012,
	        "composer": "Diplo &#38; Flinch",
	        "sample_rate": 44100,
	        "size": 8132318,
	        "location": "file://localhost/Users/mlmiller/Music/iTunes/iTunes%20Media/Music/Diplo/Express%20Yourself%20-%20EP/03%20No%20Problem%20(feat.%20Flinch%20&#38;%20My%20Name%20Is%20Kay).m4a",
	        "genre": "Dance",
	        "total_time": "218868",
	        "name": "No Problem (feat. Flinch &#38; My Name Is Kay)",
	        "date_modified": 1339608763,
	        "play_count": 16,
	        "artist": "Diplo",
	        "track_number": "3",
	        "compilation": "false",
	        "date_added": 1339608758,
	        "album": "Express Yourself - EP",
	        "album_artist": "Diplo"
	      },
	      "order": [
	        16,
	        1728
	      ],
	      "id": "1adbc6c55edfa143275ff2a781f869fd"
	    },
	    {
	      "fields": {
	        "bit_rate": 256,
	        "kind": "Purchased AAC audio file",
	        "year": 2012,
	        "composer": "Diplo &#38; Datsik",
	        "sample_rate": 44100,
	        "size": 9879323,
	        "location": "file://localhost/Users/mlmiller/Music/iTunes/iTunes%20Media/Music/Diplo/Express%20Yourself%20-%20EP/02%20Barely%20Standing%20(feat.%20Datsik%20&#38;%20Sabi).m4a",
	        "genre": "Dance",
	        "total_time": "282545",
	        "name": "Barely Standing (feat. Datsik &#38; Sabi)",
	        "date_modified": 1339608764,
	        "play_count": 20,
	        "artist": "Diplo",
	        "track_number": "2",
	        "compilation": "false",
	        "date_added": 1339608758,
	        "album": "Express Yourself - EP",
	        "album_artist": "Diplo"
	      },
	      "order": [
	        20,
	        1584
	      ],
	      "id": "1adbc6c55edfa143275ff2a781f87197"
	    },
	    {
	      "fields": {
	        "bit_rate": 256,
	        "kind": "Purchased AAC audio file",
	        "year": 2012,
	        "composer": "Diplo",
	        "sample_rate": 44100,
	        "size": 9990340,
	        "location": "file://localhost/Users/mlmiller/Music/iTunes/iTunes%20Media/Music/Diplo/Express%20Yourself%20-%20EP/01%20Express%20Yourself%20(feat.%20Nicky%20Da%20B).m4a",
	        "genre": "Dance",
	        "total_time": "277546",
	        "name": "Express Yourself (feat. Nicky Da B)",
	        "date_modified": 1339608764,
	        "play_count": 24,
	        "artist": "Diplo",
	        "track_number": "1",
	        "compilation": "false",
	        "date_added": 1339608758,
	        "album": "Express Yourself - EP",
	        "album_artist": "Diplo"
	      },
	      "order": [
	        24,
	        558
	      ],
	      "id": "dcfaf239729a172799859b0c76b52682"
	    }
	  ],
	  "bookmark": "g1AAAADaeJzLYWBgYM5gTmGQSUlKzi9KdUhJMtLLTU1M0UvOyS9NScwr0ctLLckBqmJKZEiy____fxaY4-YgwgAGSQwMbBuyiDMhjwWkowFIAc3ZDzPIAm4Qkx5JBh2AGAR3kQnCRQZZWQDl-jr5",
	  "total_rows": 7
	}
	
# Extras

##  View Collation.  
For the discussion on MapReduce, the  explanation of how keys are sorted is incredibly useful: [http://wiki.apache.org/couchdb/View_collation#Collation_Specification](http://wiki.apache.org/couchdb/View_collation#Collation_Specification)

## Pushing new Indexing Code.  
I use couchapp-python, a depricated but functional python library.

	sudo pip install couchapp
	cd ana1
	couchapp push 'https://username:pwd@username.cloudant.com/itunes1'
	


