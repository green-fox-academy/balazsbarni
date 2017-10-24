'use strict';

// Swap the values of these variables
var a = 123;
var b = 526;

a = a + b;
b = a - b;
a = a - b;

console.log(a);
console.log(b);