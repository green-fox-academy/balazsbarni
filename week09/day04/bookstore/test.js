let q = { cat: 'Sci', aut: 'joe', price: 'xy' }


let transf = function(q){

    q.forEach(function(key, value) {
     console.log(q.key, q.value)   
    })
}
var arr = Object.keys(q).map(function (key) { return q[key]; });


const transformQuery = function(query) {
    let searchKeys = (Object.keys(query))
    let searchValues = (Object.values(query))
    let string = "WHERE ";
    for (let i = 0; i < searchKeys.length; i++) {
        string += searchKeys[i] + ' = ' + searchValues[i] + ' AND ';
    }
    return string;
}

console.log(transformQuery(q))
