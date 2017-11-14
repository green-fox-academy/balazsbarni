'use strict';

const Playlist = (function() {
    let render = function(item){
        console.log(item)
        item.forEach(function(item) {
            let temp = document.querySelector('.playbody');
            let rendered = document.createElement('div');
            rendered.innerText = item.title;
            rendered.className = 'playlists';
            temp.appendChild(rendered);
        })
    };
    ajax('GET', 'playlists', render);
})();