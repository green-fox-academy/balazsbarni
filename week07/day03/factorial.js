'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(num) {
    let sumFact = 1;
    for (let i = 2; i <= num; i += 1) {
        sumFact *= i;
    }
    return sumFact;
}

console.log(factorio(4));