'use strict';

const trackList = (function() {
    let currentTrack = null;
    let star = document.querySelector('.star');
    star.addEventListener('click', function(){
        addFavourite();
    });
    
    let render = function(items) {
        let counter = 1;
        items.forEach(function(item){
            let temp = document.querySelector('.tracks');
            let rendered = document.createElement('div');
            rendered.addEventListener('click', () => {
                let trackPlay = document.getElementById('audioPlayer')
                trackPlay.src = item.path;
                document.querySelector('.title').innerText = item.title;
                document.querySelector('.artist').innerText = item.author;
                currentTrack = item;
            });
            rendered.innerText = counter + '  ' + item.title;
            rendered.className = 'track';
            temp.appendChild(rendered);
            counter ++;
        });
    };

    let convertSecs = function(s){
        return(s-(s%=60))/60+(9<s?':':':0')+s
    }

    let load = function(id, all) {
        let tracklist = document.querySelector('.tracks')
        tracklist.innerHTML = '';
        let queryParam = null;
        if (all) {
            queryParam = 'tracks';
        } else {
            queryParam = 'tracks/q?playlist_id=' + id; 
        }
        ajax('GET', queryParam , render);
    };

    let pass = function(){};

    let addFavourite = (item) => {
        let postData = {
            "title": currentTrack.title,
            "author": currentTrack.author,
            "path": currentTrack.path,
            "id": currentTrack.id
        };
        ajax('POST', 'tracks', res => {
            console.log(res)
        }, postData)
    };


    return {
        load: load
    };
})();

