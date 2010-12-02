function(doc) 
{
    if (doc && doc.url && doc.date && doc.links) {
        for (var i in doc.links) {
            emit([doc.url, doc.date[0], doc.date[1], doc.date[2], doc.links[i]], 1)
        }
    }
}
