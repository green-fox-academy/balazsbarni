'use strict!';

function createMatrix (size) {
    let matrix = [];
    for (let row = 0; row < size; row++) {
        let columns = [];
        for (let column = 0; column < size; column++) {
            if (row === column) {
                columns.push(1);
            } else {
                columns.push(0);
            }
        }
        matrix.push(columns);
    }
    return matrix;
}

console.log(createMatrix(5));