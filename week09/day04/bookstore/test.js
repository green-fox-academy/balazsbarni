let q = { category: 'sci', pgt: '50', publisher: 'xy' }



const transformQuery = function(query) {
    let searchKeys = (Object.keys(query))
    let searchValues = (Object.values(query))
    let string = "WHERE ";
    for (let i = 0; i < searchKeys.length; i++) {
        if (searchKeys[i] === 'category'){
        string += 'category.cate_descrip = "' + capitalize(searchValues[i]) + '" AND ';
    } else if (searchKeys[i] === 'publisher'){
        string += 'publisher.pub_name = "' + capitalize(searchValues[i]) + '" AND ';
    } else if (searchKeys[i] === 'plt') {
        string += 'book_price < ' + searchValues[i] + ' AND ';
    } else if (searchKeys[i] === 'pgt') {
        string += 'book_price > ' + searchValues[i] + ' AND ';
    }
}
    return string.split(" ").slice(0, -2).join(" ");
}


function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}

console.log(transformQuery(q))