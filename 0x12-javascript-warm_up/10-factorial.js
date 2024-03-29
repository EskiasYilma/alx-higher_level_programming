#!/usr/bin/node

/*
computes and prints a factorial
*/

const process = require('process');

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (String(Number(process.argv[2])) === 'NaN') {
  console.log(factorial(0));
} else {
  console.log(factorial(Number(process.argv[2])));
}
