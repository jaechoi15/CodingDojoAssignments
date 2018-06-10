// Assignment: Ninja Class III
// Part I
// Recreate the base Ninja class from scratch using ES6 classes. Your Ninja needs the following attributes:
// name
// health
// speed
// strength
// Speed and strength should be 3 by default. Health should be 100 by default. Do not worry about private variables.
// The Ninja class should have the following methods:
// sayName() - This should log that Ninja's name to the console.
// showStats() - This should show the Ninja's Strength and Speed, as well as their health.
// drinkSake() - This should add +10 Health to the Ninja

// Define the class
class Ninja {
    constructor(name) {
        this.name = name;
        this.health = 100;
        this.speed = 3;
        this.strength = 3;
    }

    // Log the Ninja's name to the console
    sayName() {
        console.log(`My ninja name is ${ this.name }`);
    }

    // Shows the Ninja's Strength and Speed, and their Health
    showStats() {
        console.log(`Name: ${this.name}, Health: ${this.health}, Speed: ${this.speed}, Strength: ${this.strength}`);
    }

    // Adds +10 Health to the Ninja
    drinkSake() {
        this.health += 10;
    }
};

// Create new instances
const ninja1 = new Ninja("Leonardo");
ninja1.sayName();
// => My ninja name is Leonardo

ninja1.showStats();
// => Name: Leonardo, Health: 100, Speed: 3, Strength: 3

ninja1.drinkSake();
ninja1.showStats();
// => Name: Leonardo, Health: 110, Speed: 3, Strength: 3


// Part II - Sensei Class
// Extend the Ninja class and create the Sensei class. A Sensei should have 200 Health, 10 speed, and 10 strength by default. In addition, a Sensei should have a new attribute called wisdom, and the default should be 10. Finally, add the speakWisdom() method. speakWisdom() should call the drinkSake() method from the Ninja class, before console.logging a wise message.

class Sensei extends Ninja {
    constructor(name) {
        super(name);
        this.wisdom = 10;
        this.health = 200;
        this.speed = 10;
        this.strength = 10;
    }

    speakWisdom() {
        super.drinkSake();
        console.log("Just do it.")
    }
};

// Create new instance
const superSensei = new Sensei("Master Splinter");

superSensei.speakWisdom();
// => Just do it.

superSensei.showStats();
// => Name: Master Splinter, Health: 210, Speed: 10, Strength: 10