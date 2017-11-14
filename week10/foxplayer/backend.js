'use strict';

var express = require('express');
var app = express();
app.use('/assets', express.static('./assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');    
});

app.get('/playlists', function(req, res) {
    let result = [
        { "id": 1, "title": "Favorites", "system": 1},
        { "id": 2, "title": "Music for programming", "system": 0},
        { "id": 3, "title": "Driving", "system": 0},
        { "id": 5, "title": "Fox house", "system": 0}]
    res.json(result);
});



  
app.listen(3000);