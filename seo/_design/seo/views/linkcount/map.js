function(doc) 
{
    if (doc && doc.url && doc.date && doc.links) {
        emit([doc.date[0], doc.date[1], doc.date[2], doc.url], doc.links.length);
    }
}
