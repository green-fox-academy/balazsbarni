'use strict';
// - Create variable named `al` and assign the value `Greenfox` to it
// - Create a function called `greet` that greets it's input parameter
//     - Greeting is printing e.g. `Greetings, dear Greenfox`
//     - Prepare for the special case when no parameters are given
// - Greet `al`

let al = 'Greenfox';

function greet(toGreet = 'Mr Anonymus') {
    console.log('Greetings, dear ' + toGreet + '!');
}

greet(al);