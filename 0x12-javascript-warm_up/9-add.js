#!/usr/bin/node

/*
prints a square
*/

const process = require('process');

function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
