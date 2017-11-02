
// Create a prison function, that has your name as a private fugutive variable
// The function should return an object that has two methods:
//  - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//  - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable

var prison = new jail(name);

function jail(name) {
    this.privateFugitive = name;
    this.timesVisited = 0;
    this.visit = function() {
        if (this.privateFugitive == '') {
            console.log('Nobody is here anymore');
        } else {
            console.log(this.privateFugitive + ' is visited ' + this.timesVisited + 'time(s)');
            this.timesVisited += 1;
        }    
    }
    this.escape = function() {
        console.log('BREAKING NEWS, ' + this.privateFugitive + 'escaped the prison');
        this.privateFugitive = '';
    }
}



const alcatraz = prison('Sad Panda');
alcatraz.visit()
alcatraz.visit()
alcatraz.escape()
alcatraz.visit()
