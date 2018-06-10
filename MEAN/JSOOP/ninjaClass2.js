// Assignment: Ninja Class II
// Complete the below challenges using the Ninja Class from the previous assignment. You may skip the functionality related to private variables.

// .punch()
// Add a new method to your Ninja class called .punch(). This method will take another Ninja instance and subtract 5 Health from the Ninja we passed in. Your .punch() should display a console message like the below example.
// const blueNinja = new Ninja("Goemon");
// const redNinja = new Ninja("Bill Gates");
// redNinja.punch(blueNinja);
// // -> "Goemon was punched by Bill Gates and lost 5 Health!"

// .kick()
// Now add a method to your Ninja class called .kick(). Kick will subtract 15 Health for each point of Strength the calling Ninja has, and like .punch() will take another Ninja instance.
// blueNinja.kick(redNinja);
// // -> "Bill Gates was kicked by Goemon and lost 15 Health!"

// Validations
// Update .punch() and .kick() so that they only accept Instances of the Ninja class. Hint: You will need to find a way to check the constructor of an instance. You will often need to consult outside documentation to find solutions for particular features.

// Define the class
function Ninja(name) {
    this.name = name;
    this.health = 100;
    const speed = 3;
    const strength = 3;
    
    // Add methods to the Ninja prototype
    // Log the Ninja's name to the console
    Ninja.prototype.sayName = function() {
        console.log("My ninja name is " + this.name + "!");
        return this;
    };

    // Shows the Ninja's Strength and Speed, and their Health
    Ninja.prototype.showStats = function() {
        console.log("Name: " + this.name + ", " + "Health: " + this.health + ", " + "Speed: " + speed + ", " + "Strength: " + strength);
        return this;
    };

    // Adds +10 Health to the Ninja
    Ninja.prototype.drinkSake = function() {
        this.health += 10;
        return this;
    };

    // Takes another Ninja instance and subtracts 5 Health from the Ninja passed in
    Ninja.prototype.punch = function(punchReceiver) {
        // Validation to only accept instances of the Ninja class
        if (punchReceiver instanceof Ninja) {
            punchReceiver.health -= 5;
            console.log(punchReceiver.name + " was punched by " + this.name + " and lost 5 Health!");
        } else {
            console.log("Not a Ninja")
        };
        return this;
    };

    // Subtracts 15 Health for each point of Strength the calling Ninja has, and like .punch() will take another Ninja instance
    Ninja.prototype.kick = function(kickReceiver) {
        // Validation to only accept instances of the Ninja class
        if (kickReceiver instanceof Ninja) {
            const kickDamage = 15 * strength;
            kickReceiver.health -= kickDamage;
            console.log(kickReceiver.name + " was kicked by " + this.name + " and lost " + kickDamage + " Health!");
        } else {
            console.log("Not a Ninja")
        };
        return this;
    };
}; // END

// // Create new instances
// const ninja1 = new Ninja("Hyabusa");

// ninja1.sayName();
// // => My ninja name is Hyabusa!

// ninja1.drinkSake().drinkSake().showStats();
// // => Name: Hyabusa, Health: 120, Speed: 3, Strength: 3

// const ninja2 = new Ninja("Subaru");

// ninja2.sayName();
// // => My ninja name is Subaru!

// ninja2.drinkSake().showStats();
// // => Name: Subaru, Health: 110, Speed: 3, Strength: 3

const blueNinja = new Ninja("Goemon");
const redNinja = new Ninja("Bill Gates");

redNinja.punch(blueNinja);
// => Goemon was punched by Bill Gates and lost 5 Health!

redNinja.showStats();
// => Name: Bill Gates, Health: 100, Speed: 3, Strength: 3

blueNinja.showStats();
// => Name: Goemon, Health: 95, Speed: 3, Strength: 3

blueNinja.kick(redNinja);
// => Bill Gates was kicked by Goemon and lost 45 Health!

redNinja.showStats();
// => Name: Bill Gates, Health: 55, Speed: 3, Strength: 3