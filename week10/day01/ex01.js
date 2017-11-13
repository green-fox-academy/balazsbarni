'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

let Animals = function(sound){
    this.soundLike = sound;
};

Animals.prototype.say = function(){
    console.log(this.soundLike);
};

let dog = new Animals('vau');
let donkey = new Animals('ia');

donkey.say();
dog.say();