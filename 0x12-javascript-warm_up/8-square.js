#!/usr/bin/node

/*
prints a square
*/

const process = require('process');

let freq = '';

if (String(Number(process.argv[2])) === 'NaN') {
  console.log('Missing size');
} else {
  if (Number(process.argv[2]) > 0) {
    for (let i = 0; i < Number(process.argv[2]); i++) {
      for (let i = 0; i < Number(process.argv[2]); i++) {
        freq += 'X';
      }
      if (i === Number(process.argv[2]) - 1) {
        break;
      } else {
        freq += '\n';
      }
    }
    console.log(freq);
  }
}
