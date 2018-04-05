var arr = ["James", "Jill", "Jane", "Jack"]

function fancyArray(symbol) {
    for (i = 0; i < arr.length; i++) {
        console.log(i + symnbol + arr[i])
    }
}

fancyArray("-->>>")