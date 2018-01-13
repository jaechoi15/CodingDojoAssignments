
        var str = "A greeting here";
        var booly = true;
        var und = undefined;
        var arr = [1, "strings", true, (1 == 0), [1,2,3]];
        var nully = null;
        var myInfo = {
            name: 'Jae',
            age: 28,
            hobbies: ['sports', 'snowboarding', 'eating']
        }
        // console.log(myInfo.name);

        // Fizzbuzz - going from 1 to a 100, print "Fizz" if the number is evenly divisible by 3...
        // print "Buzz" if evenly divisble by 5...or "FizzBuzz" if both...or the number itself if none of these
function fizzbuzz(num){
    for (var i=1; i <= num; i++){
        if (i % 5 === 0 && i % 3 === 0){
            console.log('FizzBuzz');
        }
        else if (i % 3 === 0) {
            console.log("Fizz");
        }
        else if (i % 5 === 0) {
            console.log("Buzz");
        }
        else {
            console.log(i);
        }
    }
}
        
fizzbuzz(50); 