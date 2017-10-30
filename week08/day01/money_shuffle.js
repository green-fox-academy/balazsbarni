let Shuffler = {
    cash: 10000,
    transactionCount: 1,
    pick: function() {
        this.cash -= 1000;
        this.target = {};
        if (this.transactionCount %  2 === 1) {
            this.target = Panama;
            this.target.deposit(1000);
        } else {
            this.target = Cyprus;
            this.target.deposit(1000);
        }
        this.transactionCount += 1;
        console.log(this.target.name  + ' got 1000!');
    }
}

let Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function() {
        this.cash += 1000;
    }
}

let Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function() {
        this.cash += 1000;
    }
}

Shuffler.pick();
Shuffler.pick();
Shuffler.pick();
Shuffler.pick();
Shuffler.pick();

console.log(Panama.cash);
console.log(Cyprus.cash);