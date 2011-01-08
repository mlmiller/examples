function(doc) {
    var then = new Date(Date.parse(doc['Event Date']));
    emit(doc.Make, 1);
}
