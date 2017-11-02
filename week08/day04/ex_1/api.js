'use strict';

function getGifs (readyFunc) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=BpCwzxMUOebR3q1jR6RcHS5WtMAg3gMG&q=dogs&limit=16&offset=0&rating=G&lang=en');
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            let gif = JSON.parse(xhr.responseText).data;
            gif.forEach(readyFunc)
        };
    };
    xhr.send();
};

let renderGif = (function(item){
       let tempImg = document.createElement('img');
       tempImg.dataset.pista = item.images.fixed_width.url
       tempImg.src = item.images.fixed_width_still.url;
       tempImg.addEventListener('click', function(){
           [tempImg.src, tempImg.dataset.pista] = [tempImg.dataset.pista, tempImg.src]
        //    let tempData = tempImg.src
        //    tempImg.src = tempImg.dataset.pista;
        //    tempImg.dataset.pista = tempData;
       });
       document.body.appendChild(tempImg); 
});

getGifs(renderGif);