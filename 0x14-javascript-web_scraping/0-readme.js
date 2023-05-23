#!/usr/bin/node
/*
reads and prints the content of a file.
*/

const fs = require('fs');

if (process.argv[2]) {
  fs.readFile(process.argv[2], 'utf-8', function (f, err) {
    if (err) {
      return console.log(err);
    }
    console.log(f);
  });
}
