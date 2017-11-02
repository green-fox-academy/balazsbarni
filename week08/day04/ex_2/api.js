'use strict';

function getArticles (callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=1fc7a7dbfaee49a7b9012a13b9bee39b&begin_date=19690719&end_date=19690720');
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            let article = JSON.parse(xhr.responseText).response.docs;
            console.log(article);
            article.forEach(callback);
        };
    };
    xhr.send();
};

let renderArticles = function(item) {
    let artList = document.createElement('ol');
    let headLine = document.createElement('li');
    let snippet = document.createElement('li');
    let pubDate = document.createElement('li');
    let artLink = document.createElement('a')
    artLink.href = item.web_url;
    artLink.innerText = 'Link';
    headLine.innerText = 'Headline: ' + item.headline.main;
    snippet.innerText = 'Snippet: ' + item.snippet;
    pubDate.innerText = 'Publication Date: ' + item.pub_date;
    artList.appendChild(headLine);
    artList.appendChild(snippet);
    artList.appendChild(pubDate);
    artList.appendChild(artLink);
    document.body.appendChild(artList);
}



getArticles(renderArticles);