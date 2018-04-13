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
                    <div>${element.timestamp}</div>
                </div>
            </div>`;
            postBody.appendChild(post)
            let upButton = document.getElementById('up' + element.id);
            let downButton = document.getElementById('down' + element.id);
            upButton.addEventListener('click', ()=> {
                upVote(element.id);
            })            
            downButton.addEventListener('click', ()=> {
                downVote(element.id);
            })            
            })
        }); 
    
    let load = function() {
        // let postBody = document.querySelector('.container');
        // postBody.innerHTML = '';
        ajax('GET', 'posts', render);
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
    
    return {
        load: load,
        getScore: getScore
    };

})();

posts.load()
// posts.upVote(2);
// posts.upVote(2);
// posts.getScore(2);
// posts.downVote(2);
// posts.getScore(2);