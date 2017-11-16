'use strict';

const trackList = (function() {
    
    let render = function(item) {
        let counter = 1;
        console.log(item)
        item.forEach(function(item){
            let temp = document.querySelector('.tracks');
            let rendered = document.createElement('div');
            rendered.addEventListener('click', () => {
                let trackPlay = document.getElementById('audioPlayer')
                trackPlay.src = item.path;
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

    let load = function() {
        ajax('GET', 'tracks', render);
    };



    return {
        load: load
    };
})();

trackList.load();