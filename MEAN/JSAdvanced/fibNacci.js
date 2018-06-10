function fib() {

    let num1 = 0;
    let num2 = 1;

    function nacci() {

        result = num1 + num2;
        num1 = num2;
        num2 = result;
        console.log(num1);
    }
    return nacci
  }
  
var fibCounter = fib();
fibCounter() // => "1"
fibCounter() // => "1"
fibCounter() // => "2"
fibCounter() // => "3"
fibCounter() // => "5"
fibCounter() // => "8"