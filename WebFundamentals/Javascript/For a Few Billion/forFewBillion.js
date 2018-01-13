// There is an old tale about a king who offered a servant $10,000 as a reward. The servant instead asked that for 30 days he be given an amount that would double, starting with a penny. (1 penny for the first day, 2 for the second, 4 for the third, then 8, 16, 32 pennies, and so on).

var earnings = .01;
var total = .01;

for (var i = 2; i <=10000; i++){
    earnings = earnings * 2;
    console.log("earnings:", earnings);
    total = total + earnings;
    console.log("total:", total);
    if (total == Infinity){
        console.log(i);
        break
    }
}