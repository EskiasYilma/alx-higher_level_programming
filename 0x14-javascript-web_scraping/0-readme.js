#!/usr/bin/node

const fs = require('fs');

if (process.argv[2]) {
  fs.readFile(process.argv[2], 'utf-8', function (f, error) {
    if (error) {
      return console.log(error);
    }
    console.log(f);
  });
}
