'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(num) {
    let sumTemp = 0;
    for (let i = 1; i <= num; i += 1) {
        sumTemp += i;
    }
    return sumTemp;
}

console.log(sum(3));