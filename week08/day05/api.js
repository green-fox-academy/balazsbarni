'use strict';

function getPosts (callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://secure-reddit.herokuapp.com/simple/posts');
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            let post = JSON.parse(xhr.responseText).posts;
            callback(post);
        };
    };
    xhr.send();
};

let renderPosts = function(item)  {
    console.log(item);
};

getPosts(renderPosts);