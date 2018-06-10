// Assignment: Deck of Cards

// Create a Deck class. A deck should have the following functionality:
// The Deck should contain the 52 standard cards
// The Deck should be able to shuffle
// The Deck should be able to reset
// The Deck should be able to deal a random card
// Deal should return the card that was dealt and remove it from the deck

// Now create a Player class. A Player should have the following functionality:
// The Player should have a name
// The Player should have a hand
// The Player should be able to take a card (use the deck.deal method)
// The Player should be able to discard a card

class Deck {
    constructor() {
        this.deck = [];
    }
    
    // Resets the deck of cards. Pushes all values and suits into the deck
    reset() {
        this.deck = [];
        const cardSuits = ["Hearts", "Diamonds", "Spades", "Clubs"];
        const cardValues = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"];

        for (const cardSuit of cardSuits) {
            for (const cardValue of cardValues) {
                this.deck.push(`${cardValue} of ${cardSuit}`);
            }
        }
        return this;
    } // End reset

    deal() {
        return this.deck.pop();
    } // End deal

    shuffle() {
        let lengthOfDeck = this.deck.length, t, i;

        while (lengthOfDeck) {
            i = Math.floor(Math.random() * lengthOfDeck--);
            t = this.deck[lengthOfDeck];
            this.deck[lengthOfDeck] = this.deck[i];
            this.deck[i] = t;
        }
        return this;
    }// End shuffle
} // End Class

class Player {
    constructor(name) {
        this.name = name;
        this.hand = [];
    }

    draw(deck) {
        this.hand.push(deck.deal());
        return this;
    }

    discard() {
        this.hand.pop();
        return this;
    }
}

// Create new instances
const deck1 = new Deck();
deck1.reset().shuffle();
console.log(deck1);

const player1 = new Player("Duke");
player1.draw(deck1);

console.log(player1);
// => Player { name: 'Duke', hand: [ '10 of Hearts' ] }
console.log(deck1);

player1.discard();

console.log(player1); // Displays empty hand