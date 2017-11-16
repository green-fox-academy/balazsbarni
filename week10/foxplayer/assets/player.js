'use strict';

const player = (function(){
    trackList.load();
    playList.load();
    playList.setClickHandler(trackList.load)
    playList.addPlaylistDialog();

})()