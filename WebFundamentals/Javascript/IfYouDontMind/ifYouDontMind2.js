var HOUR = 8;
var MINUTE = 30;
var PERIOD = "AM";

if (MINUTE == 5) {
    time = "It's 5 after " + (HOUR)
}
else if (MINUTE == 15) {
    time = "It's quarter after " + (HOUR)
}
else if (MINUTE == 30) {
    time = "It's half past " + (HOUR)
}
else if (MINUTE > 30) {
    time = "It's almost " + (HOUR + 1)
}
else {
    time = "It's just after " + (HOUR)
}

if (PERIOD == "AM") {
    time += " in the morning"
}
else {
    time += " in the evening"
}

console.log(time);