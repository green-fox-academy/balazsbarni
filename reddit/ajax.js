'use strict';
const url = 'http://localhost:3300/';
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

function ajax (command, urlEnd, callback, reqBody) {
    let xhr = new XMLHttpRequest();
    xhr.open(command, url + urlEnd);
    xhr.setRequestHeader('content-type', 'application/json');
    xhr.onload = function() {
        callback(JSON.parse(xhr.responseText));
    };
    let postData = null;
    if (reqBody) {
        postData = JSON.stringify(reqBody);
    };
    xhr.send(postData);
};

const test = function(item) {
    console.log(item);
  };

let getTest = function(callback){
    ajax('GET', 'posts', callback);
};

getTest(test);