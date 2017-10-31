'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}

function selectLastEvenNumber(array, callback) {
    let evenArr = array.filter(function(num){
        return num % 2 === 0;
    })
    return callback(evenArr.slice(-1)[0]);
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8