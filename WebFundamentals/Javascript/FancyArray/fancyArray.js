// Write a function that will make it print like:
// 0 -> James
// 1 -> Jill
// 2 -> Jane
// 3 -> Jack

var arr = ["James", "Jill", "Jane", "Jack"];

function fancyArray()
{
    for (var i = 0; i < arr.length; i++)
    {
        console.log(i + " -> " + arr[i]);
    }
}
fancyArray();


// Let the user pass in the symbol that will print (ex: "->", "=>", "::", "-----")

var arr = ["James", "Jill", "Jane", "Jack"];

function fancySymbol(arr, symbol)
{
    if (symbol == undefined) //If the user does not pass in a symbol, " -> " will be used as the default symbol
    {
        symbol = " -> ";
    }
    for (var i = 0; i < arr.length; i++)
    {
        console.log(i + symbol + arr[i]);
    }    
}
fancySymbol(arr);


// Have an extra parameter reversed. If the user passes true, print the elements in reverse order

var arr = ["James", "Jill", "Jane", "Jack"];

function fancySymbol(arr, symbol, reversed) 
{
    if (symbol == undefined) //If the user does not pass in a symbol, " -> " will be used as the default symbol
    {
        symbol = " -> ";
    }
    if (reversed == "yes") //If the user passes "yes", the elements will be printed in reverse order
    {
        for (var i = arr.length - 1; i >= 0; i--)
        {
            console.log (i + symbol + arr[i]);
        }
    }
    else 
    {
        for (var i = 0; i < arr.length; i++)
        {
            console.log(i + symbol + arr[i]);
        }    
    }
}
fancySymbol(arr, " => ", "yes");