#!/usr/bin/node

/*
searches the second biggest integer in the list of arguments.
*/

const process = require('process');

const array = [];

if (String(Number(process.argv[2])) === 'NaN' || process.argv.length - 2 === 1) {
  console.log(0);
} else {
  for (let i = 0; i < (process.argv.length - 2); i++) {
    array.push(Number(process.argv[i + 2]));
  }
  let x = 0;

  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < i; j++) {
      if (array[i] < array[j]) {
        x = array[i];
        array[i] = array[j];
        array[j] = x;
      }
    }
  }
  console.log(array[1]);
}
