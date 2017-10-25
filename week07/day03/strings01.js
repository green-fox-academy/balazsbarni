'use strict';

var example = "In a dishwasher far far away";

// I would like to replace "dishwasher" with "galaxy" in this example
// Please fix it for me!
// Expected ouput: In a galaxy far far away

let toReplace = example.replace('dishwasher', 'galaxy');
example = toReplace

console.log(example)