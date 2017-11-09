'use strict';
const url = 'http://localhost:3000/'

function ajax (command, endName, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open(command, url + endName);
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            callback(JSON.parse(xhr.responseText));
            console.log(JSON.parse(xhr.responseText).author);
        };
    };
    xhr.send();
};


const getTitle = function(callback) {
    ajax('GET', 'API', callback);
  };

let renderBook = (function(item){
    item.forEach(function(item) {
        let tempBook = document.createElement('p');
        tempBook.innerText = item.book_name;
        document.body.appendChild(tempBook);
    })
});

let renderTable = function(callback) {
    let mainTable = document.createElement('table');
    item.forEach(function(item){
        let tableRow = document.createElement('tr');
        let tableTitle = document.createElement('td');
        let tableAuthor = document.createElement('td');
        let tableCategory = document.createElement('td');
        let tablePublish = document.createElement('td');
        let tablePrice = document.createElement('td');
        tableTitle.innerText = item.book_name;
        tableAuthor.innerText = item.book_name;
        tableTitle.innerText = item.book_name;
        tableTitle.innerText = item.book_name;
        tableTitle.innerText = item.book_name;
        
    })
}

getTitle(renderBook);