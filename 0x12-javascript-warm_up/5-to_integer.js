#!/usr/bin/node

/*
prints a message depending of the number of arguments passed
*/

const process = require('process');

if (typeof (Number(process.argv[2])) === 'number') {
  if (String(Number(process.argv[2])) === 'NaN') {
    console.log('Not a number');
  } else {
    console.log('My number: ' + Number(process.argv[2]));
  }
} else {
  console.log('Not a number');
}
