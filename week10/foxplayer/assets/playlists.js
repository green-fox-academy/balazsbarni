'use strict';

const playList = (function() {
    
    let render = function(item){
        item.forEach(function(item) {
            let temp = document.querySelector('.playbody');
            let rendered = document.createElement('div');
            if (item.system === 0) {
                rendered.className = 'playlists';
                let noNative = document.createElement('div')
                noNative.innerText = item.title;
                let deleteSym = document.createElement('div');
                deleteSym.innerText = '×';
                deleteSym.addEventListener('click', () => {
                    plDelete(item.id);
                });
                rendered.appendChild(noNative);
                rendered.appendChild(deleteSym);
                temp.appendChild(rendered);
            } else if (item.system === 1) {
                rendered.innerText = item.title;
                rendered.className = 'playlists';
                temp.appendChild(rendered);
            }
        });
    };

    let create = function(playlistName) {
        let playlist = document.querySelector('.playbody')
        playlist.innerHTML = '';
        let postData = {"title": playlistName};
        ajax('POST', 'playlists', render, postData);
    };
    
    let load = function() {
        ajax('GET', 'playlists', render);
    };
    
    let addPlaylistDialog = function() {
        const dialogRootElement = document.querySelector('.dialog')
        const button = dialogRootElement.querySelector('button');
        const input = dialogRootElement.querySelector('input');
        const closeBtn = dialogRootElement.querySelector('div');
        const addBtn = document.querySelector('.addlist')
        dialogRootElement.style.display = 'none';

        button.addEventListener('click', () => {
            create(input.value);
            dialogRootElement.style.display = 'none';
        });

        closeBtn.addEventListener('click', () => {
            dialogRootElement.style.display = 'none';
        });

        addBtn.addEventListener('click', () => {
            dialogRootElement.style.display = 'block';
        });
    };

    let plDelete = function(id) {
        let playlist = document.querySelector('.playbody')
        playlist.innerHTML = '';
        let deleteData = {"id": id};
        ajax('DELETE', 'playlists', render, deleteData);
    };

    let highlight = function() {}

    return {
        load: load,
        create: create,
        addPlaylistDialog: addPlaylistDialog,
        delete: plDelete
    }
})();

playList.load()
playList.addPlaylistDialog()
//playList.delete('New pl')


