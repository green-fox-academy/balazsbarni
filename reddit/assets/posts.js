'use strict';

const posts = (function () {
    let render = (function(items){
        let postBody = document.querySelector('.container');
        items.forEach(element => {
            let post = document.createElement('div');
            post.innerHTML = `
            <div class="post">
                <div class="vote">
                    <div id= "up${element.id}">up</div>
                    <div id="score${element.id}">${element.score}</div>
                    <div id= "down${element.id}">down</div>
                </div>
                <div class="postbody">
                    <div>${element.title}</div>
                    <div>${element.url}</div>
                    <div>posted at: ${getDate(element.timestamp)}</div>
                </div>
                <div id="delete${element.id}">delete post</div>
            </div>`;
            postBody.appendChild(post)
            let upButton = document.getElementById('up' + element.id);
            let downButton = document.getElementById('down' + element.id);
            let deleteButton = document.getElementById('delete' + element.id);
            upButton.addEventListener('click', ()=> {
                upVote(element.id);
                })            
            downButton.addEventListener('click', ()=> {
                downVote(element.id);
                })
            deleteButton.addEventListener('click', ()=> {
                deletePost(element.id);
                })            
            })
        }); 
    
    let load = function() {
        ajax('GET', 'posts', render);
        postWindow();
    };

    let test = function(item) {
        // console.log(item);
    }

    
    let upVote = function(id) {
        ajax('PUT', 'upvote/' + id, test);
        getScore(id);
    }
    
    let downVote = function(id) {
        ajax('PUT', 'downvote/' + id, test);
        getScore(id);
    }
    
    let getScore = function(id) {
        ajax('GET', 'search/' + id , setScore);
    }
    
    let setScore = function(element) {
        document.getElementById('score' + element[0].id).innerText = element[0].score;
    }

    let getDate = function(timestamp) {
        var date = new Date(timestamp).getDate();
        var month = new Date(timestamp).getMonth()+1;
        var year = new Date(timestamp).getFullYear();
        var hour = new Date(timestamp).getHours();
        var min = new Date(timestamp).getMinutes();
        // var sec = new Date(timestamp).getSeconds();
        var original_date= month + '/' + date+'/' + year + ' at ' + hour + ':' + min;
        return original_date;
    }

    let postWindow = function() {
        let postBody = document.querySelector('.post');
        postBody.innerHTML = 
            `<h1>Add post</h1>
            <p>title:</p>
            <input id="posttitle" type="text">
            <p>post:</p>
            <input id="postbody" type="text">
            <button id="submit">Submit</button>`;
        let button = document.getElementById('submit');
        let title = document.getElementById('posttitle');
        let url = document.getElementById('postbody');
        button.addEventListener('click', ()=> { 
            createPost(title.value, url.value);
            title.value = '';
            url.value = '';
        })
    }

    let createPost = function(title, url) {
        let postData = {'title': title,
                        'url': url
                        };                    
        ajax('POST', 'posts', test, postData);
        reRender()
    };

    let deletePost = function(postId) {
        let deleteData = {"id": postId};
        ajax('DELETE', 'posts', test, deleteData);
        reRender();
    }

    let reRender = function() {
        document.querySelector('.container').innerHTML = '';
        ajax('GET', 'posts', render);
    }

    return {
        load: load
    };

})();

posts.load();
// ajax('POST', 'posts', test, {'title': 'BbBBBBB', 'url': 'AAAAAAAA'})
// posts.upVote(2);
// posts.upVote(2);
// posts.getScore(2);
// posts.downVote(2);
// posts.getScore(2);