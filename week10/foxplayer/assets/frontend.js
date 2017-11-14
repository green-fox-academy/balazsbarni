'use strict';
const url = 'http://localhost:3000/playlists';

function ajax ( callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.onload = function() {
        callback(JSON.parse(xhr.responseText));
    };
    xhr.send();
};

const test = function(item) {
    console.log('ok');
  };

ajax(test);



