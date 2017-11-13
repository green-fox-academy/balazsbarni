'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

let Rectangle = function(base, heigth) {
    this.base = base;
    this.heigth = heigth;
};

Rectangle.prototype.getArea = function() {
    return this.base * this.heigth;
};

Rectangle.prototype.getCirc = function() {
    return 2 * (this.base + this.heigth); 
};

let rectOne = new Rectangle(10, 5);
console.log(rectOne.getArea());
console.log(rectOne.getCirc());