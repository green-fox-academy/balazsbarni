'use strict';

let isAnagram = function(str1, str2){
    if (typeof str1 || typeof str2 !== 'string'){
        throw 'bibivan';
    }
    let arr1 = str1.split('');
    let arr2 = str2.split('');
    let sortArr1 = arr1.sort().join('');
    let sortArr2 = arr2.sort().join('');
    return sortArr1 == sortArr2;
}

module.exports = isAnagram;
