'use strict';
const url = 'http://localhost:3000/';

function ajax (command, urlEnd, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open(command, url + urlEnd);
    xhr.onload = function() {
        callback(JSON.parse(xhr.responseText));
    };
    xhr.send();
};

const test = function(item) {
    console.log(item);
  };

let getTest = function(callback){
    ajax('GET', 'playlists', callback);
};
//getTest(test);





