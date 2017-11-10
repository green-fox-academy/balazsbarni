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

const getTable = function(callback) {
    ajax('GET', 'books', callback);
  };

let renderBook = (function(item){
    item.forEach(function(item) {
        let tempBook = document.createElement('p');
        tempBook.innerText = item.book_name;
        document.body.appendChild(tempBook);
    })
});

let renderTable = (function(item){
    let mainTable = document.createElement('table');
    item.forEach(function(item){
        let tableRow = document.createElement('tr');
        let name = document.createElement('td');
        name.innerText = item.book_name;
        let author = document.createElement('td');
        author.innerText = item.aut_name;
        let cate = document.createElement('td');
        cate.innerText = item.cate_descrip;
        let pub = document.createElement('td');
        pub.innerText = item.pub_name;
        let price = document.createElement('td');
        price.innerText = item.book_price;
        tableRow.appendChild(name);
        tableRow.appendChild(author);
        tableRow.appendChild(cate);
        tableRow.appendChild(pub);
        tableRow.appendChild(price);
        mainTable.appendChild(tableRow);
        document.body.appendChild(tableRow);
    });
})

getTable(renderTable);