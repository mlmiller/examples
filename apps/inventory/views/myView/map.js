function(doc) {
    if (doc.name && doc.amount) {
        emit(doc._id, doc);
    }
}