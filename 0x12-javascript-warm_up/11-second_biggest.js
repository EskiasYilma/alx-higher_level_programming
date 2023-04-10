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
  console.log(array.sort()[1]);
}
