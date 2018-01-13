//Create a function that can take a start point, end point, and skip amount, to print all numbers in the range.

function printRange(start,end,skip)
{
    for (var i = start; i < end; i += skip)
    {
        console.log(i);
    }   
}
printRange(-2,10,3);

//Bonus:
// Make sure it works for negative numbers
// If the user doesn't pass a skip amount, make it default to 1 (printRange(4, 8); would print 4, 5, 6, 7)
// If the user doesn't pass an end point, make it start at 0, and end at the first (printRange(4); would print 0, 1, 2, 3)

function printRangeBonus(start,end,skip)
{
    if (!skip)
    {
        skip = 1;
    }
    if (!end)
    {
        end = start;
        start = 0;
    }
    for (var i = start; i < end; i += skip)
    {
        console.log(i);
    }
}
printRangeBonus(4);