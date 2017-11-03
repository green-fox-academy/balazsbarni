'use strict';

class Animal {
    constructor() {
        this.hunger = 5;
        this.thirst = 5;
    }

    eat() {
        this.hunger -= 1;
    }

    drink() {
        this.thirst -= 1;
    }

    play() {
        this.hunger -= 1;
        this.thirst -= 1;
    }
}

class Farm {
    constructor(slots) {
        this.slots = slots;
        this.animals = [];
        this.fill();
    }
    
    fill() {
        while (this.slots > this.animals.length) {
             this.animals.push(new Animal());
        }
    }

    breed() {
        if (this.slots > this.animals.length  && Math.random() <= 0.5) {
            this.animals.push(new Animal());
            if (this.slots > this.animals.length  && Math.random() <= 0.7) {
                this.animals.push(new Animal());
            }
        }
    }

    slaughter() {
        this.toEat = 0;
        for (let i = 1; i < this.animals.length; i +=1) {
            if (this.animals[i].hunger < this.animals[this.toEat].hunger) {
                this.toEat = i;
            };
        } 
        this.animals.splice(this.toEat, 1);
    }

    report() {
        if (this.animals.length > 0) {
            console.log('The farm has ' + this.animals.length + ' living animals, we are not bancrupt!');
        } else {
            console.log('The farm has no living animals, we are bankrupt!');
        }
    }


    progress() {
        for (let i = 0; i < this.animals.length; i ++) {
            if (Math.random() <= 0.5) {
                this.animals[i].eat();
            }
        }

        for (let i = 0; i < this.animals.length; i ++) {
            if (Math.random() <= 0.5) {
                this.animals[i].drink();
            }
        }

        for (let i = 0; i < this.animals.length; i ++) {
            if (Math.random() <= 0.5) {
                this.animals[i].play();
            }
        }
    
        this.slaughter();
        this.breed();
        this.dailyReport()
    } 


    
    dailyReport() {
        if (this.animals.length === 0) {
            console.log('Bancrupt:(')
            myFarm.disabled = true;
        } else if (0 < this.animals.length < this.slots) {
            console.log('The farm has ' + this.animals.length + ' living animals, we are not bancrupt!')
        } else if (this.animals.length === this.slots) {
            console.log('Full')
        }
    }
}

let cowFarm = new Farm(3);
let myFarm = document.querySelector('button');
myFarm.addEventListener('click', cowFarm.progress.bind(cowFarm));








