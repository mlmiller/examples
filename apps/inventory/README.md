# inventory

inventory is a CouchDB application that was created from the content from https://www.ibm.com/developerworks/web/library/wa-couchdb/.  Here we have simply bundled this for distribution via the couchapp framework for simple installation.  This is a simple example of an application to create and track inventory.

## Requirements

cloudant hosted account (sign up at <https://cloudant.com/#!/solutions/cloud>) or stock CouchDB, couchapp

## Install

<pre><code>
git clone git@github.com:mlmiller/examples.git
cd inventory
curl -X PUT 'http://&lt;user&gt;:&lt;pwd&gt;&lt;user&gt;.cloudant.com:5984/&lt;dbname&gt;'
couchapp push 'http://&lt;user&gt;:&lt;pwd&gt;&lt;user&gt;.cloudant.com:5984/&lt;dbname&gt;'

To configure the application display and behavior, modify the files:

    _attachments/index.html
    _attachments/script.js
    
To add a new view add a new directory under views.  The view name will be the name of the directory (ala myViews) and then you can simply write map.js (and reduce.js if required) in that directory.

Now view your app at http://&lt;user&gt;:&lt;pwd&gt;&lt;user&gt;.cloudant.com:5984/&lt;dbname&gt;/_design/myDesign/index.html

