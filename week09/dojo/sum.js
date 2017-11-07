'use strict';

let tuSum = [2,3,4,5];

let sum = function(nums) {
    let sumAll = 0;
    nums.forEach(function(element) {
        if (typeof element !== 'number'){
            throw 'nagybajvan!!';
        }
        sumAll += element;
    });
    return sumAll;
}


sum(tuSum);

module.exports = sum;