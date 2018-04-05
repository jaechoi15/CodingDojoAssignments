// function printRange(x, y, z) {
//     for (var i=x; i<y; i+=z) {
//         console.log(i);
//     }
// }

// printRange(2, 10, 2);


function printRangeBonus(x, y, z) {
    if (!z) {
        z = 1;
    }
    if (!y) {
        y = 0;
    }
    for (var i=x; i<y; i+=z) {
        console.log(i);
    }
}

printRangeBonus(4)