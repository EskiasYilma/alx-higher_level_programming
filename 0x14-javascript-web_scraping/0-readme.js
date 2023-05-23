#!/usr/bin/node
/*
reads and prints the content of a file.
*/

const file = require('fs');

if (process.argv[2]) {
  file.readFile(process.argv[2], 'utf-8', function (f, err) {
    if (err) {
      return console.log(err);
    }
    console.log(f);
  });
}
