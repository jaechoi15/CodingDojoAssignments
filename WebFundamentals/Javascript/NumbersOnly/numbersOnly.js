//Make a function that copies an array, ONLY accepting the items that are numbers.
//It should return a new array

var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);
// newArray is [1, -3, 0.5]

function copyArray(newArray)
{
    for (var i = 0; i < newArray.length; i++)
    {
        if (typeof newArray[i] === "string")
        {
            newArray = newArray[i].pop();
            return newArray;
        }
        else
        {
            return newArray;
        }
    }
}
copyArray();