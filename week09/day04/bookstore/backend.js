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
    conn.query('SELECT book_name FROM book_mast;', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});


conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});





app.listen(3000);