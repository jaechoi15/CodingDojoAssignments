var earnings = .01
var total = .01

for (var i = 2; i < 10001; i++) {
    earnings = earnings * 2
    console.log("earnings: ", earnings)
    if (earnings == Infinity) {
        console.log(i)
        break
    }
}