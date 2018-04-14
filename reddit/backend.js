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

app.use('/assets', express.static('./assets'));
app.use(express.json());

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

app.get('/search/:score', function(req, res) {
    connection.query('SELECT id, score FROM posts WHERE id="' + req.params.score + '";', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

app.put('/upvote/:id', function(req, res) {
    connection.query('UPDATE posts SET score = score + 1 WHERE id ="' + req.params.id + '";', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

app.put('/downvote/:id', function(req, res) {
    connection.query('UPDATE posts SET score = score - 1 WHERE id ="' + req.params.id + '";', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

app.post('/posts', function(req, res) {
    connection.query('INSERT INTO posts (title, url)  VALUES("' + req.body.title +'", "' + req.body.url + '");', function(error, result) {
        if(error) {
            console.log(error.toString());
        }
        res.json({'Result': 'success'});
        });
    });

    app.delete('/posts', function(req, res) {
        connection.query('DELETE FROM posts WHERE id="' + req.body.id +'";', function(error, result) {
            if(error) {
                console.log(error.toString());
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
  
app.listen(3300);