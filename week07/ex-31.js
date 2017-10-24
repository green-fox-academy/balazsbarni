'use strict';

var lineCount = 6;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is
let space = ' ';
let percent = '%'

for (let i = 0; i < lineCount; i += 1) {
    if (i === 0 || i === lineCount - 1) {
        console.log(percent.repeat(lineCount));
    } else console.log(percent + space.repeat(lineCount - 2) + percent);
}