'use strict';

var lineCount = 11;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

for (let i = 0; i < lineCount / 2; i += 1) {
    let space = ' ';
    let star = '*'
    console.log(space.repeat(lineCount / 2 - i) + star.repeat(2 * i + 1));
}
for (let i = 0; i < lineCount / 2 - 1; i += 1) {
    let space = ' ';
    let star = '*'
    console.log(space.repeat(i + 1) + star.repeat(lineCount - i * 2 - 2));
}
