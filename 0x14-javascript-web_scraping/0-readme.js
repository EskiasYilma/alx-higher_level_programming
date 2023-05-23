#!/usr/bin/node
/*
reads and prints the content of a file.
*/

const file = require('fs');

file.readFile(process.argv[2], 'utf-8', function (f, err) {
  if (err) {
    console.log(err);
  } else {
    console.log(f);
  }
});
