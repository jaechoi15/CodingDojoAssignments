// Assignment I: JavaScript Library
// Finish the five methods attached to the _ object to create your own custom library.  The purpose of this assignment is to show how a simple JavaScript library can be made. 

var _ = {
    map: function(arr, myCallback) {
      let result = [];
      for (let i = 0; i < arr.length; i++) {
          result.push(myCallback(arr[i]));
      }
      return result;
    },
    reduce: function(arr, myCallback, memo) { 
        let el = 0;
        if(!memo){
            let memo = arr[0];
            el = 1;
        }
        for(let i = el; i < arr.length; i++) {
            let memo = myCallback(arr[i], memo);
        }
        return memo;
    },
    find: function(arr, myCallback) {   
        for (let i = 0; i < arr.length; i++) {
            if (myCallback(arr[i])) {
                return arr[i];
            }
        }
    },
    filter: function(arr, myCallback) { 
        let result = [];
        for (let i = 0; i < arr.length; i++) {
            if (myCallback(arr[i])) {
                result.push(arr[i]);
            }
        }
      return result;
    },
    reject: function(arr, myCallback) { 
        let result = [];
        for (let i = 0; i < arr.length; i++) {
            if (!myCallback(arr[i])) {
                result.push(arr[i]);
            }
        }
        return result;
    }
  }

 // Filter
var evens = _.filter([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(evens); // => [2,4,6].

// Reject
var odds = _.reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(odds); // => [1, 3, 5]

// Find
var even = _.find([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(even); // => 2

// Reduce
var sum = _.reduce([1, 2, 3], function(memo, num){ return memo + num; }, 0);
console.log(sum); // => 6

// Map
var map1 = _.map([1, 2, 3], function(num){ return num * 3; });
console.log(map1); // => [3, 6, 9]

var map2 = _.map({one: 1, two: 2, three: 3}, function(num, key){ return num * 3; });
console.log(map1); // => [3, 6, 9]
