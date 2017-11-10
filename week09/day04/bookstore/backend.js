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

app.get('/API', function(req, res) {
    conn.query('SELECT * FROM book_mast;', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

app.get('/books', function(req, res) {
    if (req.query === {}){
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
        let search = req.query.category
        let searchParam = 'WHERE category.cate_descrip = \"' + search +'\"';
        console.log(searchParam);
        conn.query(`
        SELECT book_mast.book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast
        LEFT JOIN author ON author.aut_id = book_mast.aut_id
        LEFT JOIN category ON category.cate_id = book_mast.cate_id
        LEFT JOIN publisher ON publisher.pub_id = book_mast.pub_id
        ${searchParam}
        `, function(error, result) {
            if(error) {
                console.log(error.toString());
            }
            res.json(result);    
        });
    };    
});




conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.listen(3000);