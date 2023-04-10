#!/usr/bin/node

/*
prints a message depending of the number of arguments passed
*/

const process = require('process');

if (process.argv.length - 2 > 1) {
  console.log('Arguments found');
} else if (process.argv.length - 2 === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
