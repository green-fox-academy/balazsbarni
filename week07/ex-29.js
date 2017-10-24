'use strict';

var lineCount = 8;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (let i = 0; i < lineCount; i += 1) {
    let space = ' ';
    let star = '*'
    console.log(space.repeat(lineCount - i) + star.repeat(2 * i + 1));
}