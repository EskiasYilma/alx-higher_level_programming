#!/usr/bin/node

/*
prints a message depending of the number of arguments passed
*/

const process = require('process');

console.log(process.argv[2] + ' is ' + process.argv[3]);
