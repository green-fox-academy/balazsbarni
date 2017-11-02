'use strict';

function getGifs (readyFunc) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=BpCwzxMUOebR3q1jR6RcHS5WtMAg3gMG&q=dogs&limit=16&offset=0&rating=G&lang=en');
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            let gif = JSON.parse(xhr.responseText);
            readyFunc(gif)
        };
    };
    xhr.send();
};

getGifs(function(items){
    let imgArr = document.querySelectorAll('img')
    for (let i = 0; i < items.data.length; i++) { 
        imgArr[i].setAttribute('src', items.data[i].images.fixed_width_still.url);
        imgArr[i].addEventListener('click', function(){
            imgArr[i].setAttribute('src', items.data[i].images.fixed_width.url);
        });   
    } 
});
