// Assignment: Ninja Class
// Create a new class called Ninja with the following attributes:
//  name
//  health
//  speed (private)
//  strength (private)
// Speed and strength should be 3 by default. Health should be 100 by default.
// The Ninja class should have the following methods:
//  sayName() - This should log that Ninja's name to the console.
//  showStats() - This should show the Ninja's Strength and Speed, as well as their health.
//  drinkSake() - This should add +10 Health to the Ninja
// Example Outputs
// const ninja1 = new Ninja("Hyabusa");
// ninja1.sayName();
// // -> "My ninja name is Hyabusa!"
// ninja1.showStats();
// // -> "Name: Hayabusa, Health: 100, Speed: 3, Strength: 3"

// Define the class
function Ninja(name) {
    this.name = name;
    this.health = 100;
    var speed = 3;
    var strength = 3;
    
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
};

// Create new instances
const ninja1 = new Ninja("Hyabusa");

ninja1.sayName();
// => My ninja name is Hyabusa!

ninja1.drinkSake().drinkSake().showStats();
// => Name: Hyabusa, Health: 120, Speed: 3, Strength: 3

const ninja2 = new Ninja("Subaru");

ninja2.sayName();
// => My ninja name is Subaru!

ninja2.drinkSake().showStats();
// => Name: Subaru, Health: 110, Speed: 3, Strength: 3