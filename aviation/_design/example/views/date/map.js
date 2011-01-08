function(doc) {
    var then = new Date(Date.parse(doc['Event Date']));
    var fatalities = 0;
    if (doc['Total Fatal Injuries']!="") 
    {
        fatalities = parseInt(doc['Total Fatal Injuries']);
    }
    emit([then.getFullYear(), then.getMonth()], [1, fatalities]);
}
