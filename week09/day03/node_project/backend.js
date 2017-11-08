'use strict';

var express = require('express');
var app = express();
app.use('/assets', express.static('assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');    
});

app.get('/doubling', function(req, res) {
    var toDoubleAnything = req.query.input;
    let toDouble = parseInt(toDoubleAnything);
    if (!toDouble){
        res.json({
            "error": "Please provide an input!"
        });
    } else {
        res.json({
            'received' : toDouble,
            'result' : toDouble * 2
        });
    };
});

app.listen(8080);