'use strict';

var express = require('express');
var mysql = require("mysql");
var app = express();
var conn = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "password",
  database: "bookstore"
});

app.use('/assets', express.static('./assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');    
});

app.get('/raw_data', function(req, res) {
    conn.query('SELECT * FROM book_mast;', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

app.get('/books', function(req, res) {
    if (!req.query){
        conn.query(`
        SELECT book_mast.book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast
        LEFT JOIN author ON author.aut_id = book_mast.aut_id
        LEFT JOIN category ON category.cate_id = book_mast.cate_id
        LEFT JOIN publisher ON publisher.pub_id = book_mast.pub_id
        `, function(error, result) {
            if(error) {
                console.log(error.toString());
            }
            res.json(result);    
        });    
    } else {
        let searchFor = transformQuery(req.query);
        conn.query(`
        SELECT book_mast.book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast
        LEFT JOIN author ON author.aut_id = book_mast.aut_id
        LEFT JOIN category ON category.cate_id = book_mast.cate_id
        LEFT JOIN publisher ON publisher.pub_id = book_mast.pub_id
        ${searchFor}
        `, function(error, result) {
            if(error) {
                console.log(error.toString());
            }
            res.json(result);    
        });
    };    
});

const transformQuery = function(query) {
    let searchKeys = (Object.keys(query))
    let searchValues = (Object.values(query))
    let string = "WHERE ";
    for (let i = 0; i < searchKeys.length; i++) {
        if (searchKeys[i] === 'category'){
        string += 'category.cate_descrip = "' + capitalize(searchValues[i]) + '" AND ';
    } else if (searchKeys[i] === 'publisher'){
        string += 'publisher.pub_name = "' + capitalize(searchValues[i]) + '" AND ';
    } else if (searchKeys[i] === 'plt') {
        string += 'book_price < "' + searchValues[i] + '" AND ';
    } else if (searchKeys[i] === 'pgt') {
        string += 'book_price > "' + searchValues[i] + '" AND ';
    }
}
    return string.split(" ").slice(0, -2).join(" ");
}


function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}


conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.listen(3000);