'use strict';

var test = require('tape');
var getApple = require('./apples.js');

test('return apple', function(t){
    var actual = getApple();
    var expected = 'apple';

    t.equal(actual, expected);
    t.end();
});





