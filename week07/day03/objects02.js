'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function whoRich (dict) {
    let richStuds = [];
    dict.forEach(function(stud) {
        if (stud.candies > 4) {
            richStuds.push(stud.name)
        }
    })
    console.log(richStuds);
}

whoRich(students);

function avgCandy (dict) {
    let candySum = 0;
    dict.forEach(function(stud) {
        candySum += stud.candies;
    })
    return console.log(candySum / dict.length);
}

avgCandy(students);