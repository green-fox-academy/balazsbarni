'use strict';

var test = require('tape');
var isAnagram = require('./anagram.js');

test('Two normalo stringo', function(t){
    var actual = isAnagram('ab', 'ba');
    var expected = true;

    t.equal(actual, expected);
    t.end();
})

test('Two non equallo stringo', function(t){
    var actual = isAnagram('ab', 'bb');
    var expected = false;

    t.equal(actual, expected);
    t.end();
})

test('Two emptyo stringo', function(t){
    var actual = isAnagram('', '');
    var expected = true;

    t.equal(actual, expected);
    t.end();
})

test('Two emptyo stringo', function(t){
    var actual = isAnagram(1, 'cv');
    var expected = true;

    t.equal(actual, expected);
    t.end();
})