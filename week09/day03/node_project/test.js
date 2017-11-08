let sum = function toSum(num){
    summNum = 0;
    while (num > 0) {
        summNum += num;
        num -= 1;
    };
    return summNum;
};

console.log(sum(2));

let factor = function(num){
    factNum = 1;
    while (num > 0) {
        factNum *= num;
        num -= 1;
    };
    return factNum;    
};

console.log(factor(3));