# inventory

inventory is a CouchDB application that was created from the content from https://www.ibm.com/developerworks/web/library/wa-couchdb/.  Here we have simply bundled this for distribution via the couchapp framework for simple installation.  This is a simple example of an application to create and track inventory.

## Requirements

cloudant hosted account (sign up at <https://cloudant.com/#!/solutions/cloud>) or stock CouchDB, couchapp

## Install

<pre><code>
cd inventory
couchapp push 'http://<user>:<pwd>@<user>.cloudant.com:5984/<db>'

To configure the application display, modify the file:

    _attachments/index.html

Now view your app at
    http://&lt;user&gt;.cloudant.com:5984/&lt;db&gt;/_design/myDesign/index.html

