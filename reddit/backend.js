'use strict';

var express = require('express');
var mysql = require('mysql');
var app = express();
var connection = mysql.createConnection({
    host: "localhost",
    user: "'root'",
    password: "password",
    database: "reddit"
});

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');    
});

app.get('/hello', function(req, res) {
    res.json({
        'response': 'hello'
    })
});

app.get('/posts', function(req, res) {
    connection.query('SELECT * FROM posts;', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

connection.connect(function(err){
    if(err){
      console.log("Error connecting to Db");
      return;
    }
    console.log("Connection established");
  });
  
app.listen(3300);