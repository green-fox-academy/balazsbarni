'use strict';

var express = require('express');
var mysql = require('mysql');
var app = express();
var connection = mysql.createConnection({
    host: "localhost",
    user: "'root'",
    password: "password",
    database: "music"
});

app.use('/assets', express.static('./assets'));
app.use(express.json());

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');    
});

app.get('/playlists', function(req, res) {
    connection.query('SELECT * FROM playlists;', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

app.post('/playlists', function(req, res) {
    connection.query('INSERT INTO playlists (playlist, system)  VALUES("' + req.body.playlist +'", 0);', function(error, result) {
        if(error) {
            console.log(error.toString());
        }
        res.json({'Result': 'success'});
        });
    });

app.delete('/playlists', function(req, res) {
    connection.query('DELETE FROM playlists WHERE id="' + req.body.id +'";', function(error, result) {
        if(error) {
            console.log(error.toString());
        }
        res.json({'Result': 'success'});
        });
    });

app.get('/tracks', function(req, res) {
    connection.query('SELECT * FROM tracks;', function(error, result){
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
  
app.listen(3000);