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
app.use('/music', express.static('./music'));
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

app.get('/tracks/q', function(req, res) {
    console.log(req.query.playlist_id);
    connection.query('SELECT * FROM tracks WHERE playlist_id="' + req.query.playlist_id + '";', function(error, result){
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

app.post('/tracks', function(req, res) {
    let querySQL = 'INSERT INTO tracks (id, title, author, path, playlist_id) VALUES( null, ?, ? ,? , 1)';
    connection.query( querySQL, [req.body.title, req.body.author, req.body.path], function(error, result) {
        if(error) {
            res.json({'Result': 'SQL error'});
            console.log(error.toString());
            return;
        }
        res.json({'Result': 'success'});
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