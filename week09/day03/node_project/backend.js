'use strict';

var express = require('express');
var app = express();

app.use('/assets', express.static('./assets'));
app.use(express.json());

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

app.post('/dountil/:what', function(req, res) {
    let operate = req.params.what;
    let result = 0;
    if (!req.body.until) {
        res.json({
            "error": "Please provide a number!"
        });
    } else {
        if (operate === 'sum') {
            result = sum(req.body.until)
        } else if (operate === 'factor') {
            result = factor(req.body.until)
        };
        res.json({
            'result': result
            });    
        };
});

let sum = function(num){
    let summNum = 0;
    while (num > 0) {
        summNum += num;
        num -= 1;
    };
    return summNum;
};

let factor = function(num){
    let factNum = 1;
    while (num > 0) {
        factNum *= num;
        num -= 1;
    };
    return factNum;    
};

app.listen(8080);