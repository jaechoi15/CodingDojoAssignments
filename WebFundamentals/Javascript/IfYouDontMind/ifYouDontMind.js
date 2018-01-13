var HOUR = 8;
var MINUTE = 31;
var PERIOD = "PM";

if (MINUTE > 30){
    time = "It's almost " + (HOUR+1);
}
else {
    time = "It's just after " + HOUR;
}

if (PERIOD == "AM"){
    time = time + " in the morning."
}
else {
    time = time + " in the evening."
}
console.log(time);