// Let's play the slots!
// Make a function that takes a number of quarters (1 quarter = 1 game).
// There is a 1 in 100 chance to win the slot machine (which will give you between 50 - 100 quarters -- use Math.random and Math.floor to pick a random number of coins).
// While the user still has quarters, use Math.random to determine if they won.


var win = Math.floor(Math.random()*100);
var reward = Math.random()*50 + 50;

function playSlots(numQuarters)
{
    for (var i = numQuarters; i > 0; i--)
    {
        if (win == 1)
        {
            numQuarters = numQuarters + reward;
            // return reward + numQuarters;
            console.log("You won " + Math.floor(reward) + " quarters!");
        }
        else 
        {   
            numQuarters = numQuarters - 1;
            console.log("BETTER LUCK NEXT TIME!");
        }
    }
}
playSlots(5);


// var win = Math.floor(Math.random()*5);
// var reward = Math.random()*50 + 50;

// function playSlots(numQuarters)
// {
//     for (var i = numQuarters; i > 0; i--)
//     {
//         if (win == 1)
//         {
//             numQuarters = numQuarters + reward;
//             // return reward + numQuarters;
//             console.log("You won " + Math.floor(reward) + " quarters!");
//         }
//         else 
//         {   
//             numQuarters = numQuarters - 1;
//             console.log("BETTER LUCK NEXT TIME!");
//         }
//     }
// }
// playSlots(5);


// Bonus:
// Let the user pass the number they are willing to leave
// (ex: If they won the lottery and still have 40 coins, they will keep playing until they have collected 200 coins)