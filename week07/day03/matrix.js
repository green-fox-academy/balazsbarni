'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

let martixSize = 6;
let matrixDraw = [];

for (let i = 0; i < martixSize; i += 1) {
    let matrixLine = [];
    for (let j = 0; j < martixSize; j += 1){
        if (j === martixSize - i - 1) {
            matrixLine.push(1);
        } else {
            matrixLine.push(0);   
        }
    }
    matrixDraw.push(matrixLine);
}

console.log(matrixDraw);