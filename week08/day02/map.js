'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

function countE (item) {
    let eCount = 0;
    let itemArr = item.split('');
    itemArr.forEach(function(i) {
        if (i === 'e') {
            eCount ++;
        }
    });
    return eCount;
}

//console.log(countE('meme'));

let eFruits = fruits.map(countE);
console.log(eFruits);