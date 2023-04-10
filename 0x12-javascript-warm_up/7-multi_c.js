#!/usr/bin/node

/*
prints x times “C is fun”
*/

const process = require('process');

if (String(Number(process.argv[2])) === 'NaN') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
