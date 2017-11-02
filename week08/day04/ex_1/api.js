'use strict';

function getGifs () {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=BpCwzxMUOebR3q1jR6RcHS5WtMAg3gMG&q=star wars&limit=16&offset=0&rating=G&lang=en');
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            let id = 0;
            let gif = JSON.parse(xhr.responseText);
            for (let i = 0; i < gif.data.length; i ++) {
                document.getElementById(i).setAttribute('src', gif.data[i].images.fixed_width_still.url);
                id ++;
            };
        };
    };
    xhr.send();
};

function getGifsMove(id) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=BpCwzxMUOebR3q1jR6RcHS5WtMAg3gMG&q=star wars&limit=16&offset=0&rating=G&lang=en');
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            let gif = JSON.parse(xhr.responseText);
            document.getElementById(id).setAttribute('src', gif.data[id].images.fixed_width.url);
        };
    };
    xhr.send();
};

let imgArr = document.querySelectorAll('img')
for (let i = 0; i < imgArr.length; i ++) {
    document.getElementById(i).addEventListener('click', function(){
        getGifsMove(i);
    });
};


getGifs();




