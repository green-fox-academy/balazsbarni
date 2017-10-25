'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer() {
    let inline = '';
    for(let i = 0; i < arguments.length; i += 1) {
        inline += arguments[i] + ' ';
     }
    console.log(inline); 
}

printer('kutya', 'macska', 'elefant');