'use strict';

var express = require('express');
var app = express();
app.use('/assets', express.static('./assets'));

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

app.get('/greeter', function(req, res) {
    var name = req.query.name;
    var title = req.query.title;
    if (!name) {
        res.json({
            "error": "Please provide a name!"
        });
    } else if (!title) {
        res.json({
            "error": "Please provide a title!"
        });
    } else {
        res.json({
            "welcome_message": "Oh, hi there " + name + ", my dear " + title +"!"
        });
    };
});

app.get('/appenda/:appendable', function(req, res){
    res.json({
        "appended": req.params.appendable + 'a'
    });
});

app.listen(8080);