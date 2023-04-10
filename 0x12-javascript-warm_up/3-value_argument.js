#!/usr/bin/node

/*
prints a message depending of the number of arguments passed
*/

const process = require('process');

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
