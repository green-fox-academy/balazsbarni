'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer() {
    console.log.apply(this, arguments);
}

printer('kutya', 'macska', 'elefant');