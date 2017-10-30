'use strict';

class Sharpie {
    constructor(color, width) {
        this.color = color;
        this.width = width;
        this.inkAmount = 100;
    }

    use() {
        this.inkAmount -= this.width;
    }
};

let blueSharp = new Sharpie('blue', 10);

let useSharpie = function(sharpie) {
    while (sharpie.inkAmount > 0) {
        sharpie.use();
        console.log(blueSharp.inkAmount);
    };
};

useSharpie(blueSharp);