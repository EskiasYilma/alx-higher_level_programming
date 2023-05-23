#!/usr/bin/node
const req = require('request');
const fs = require('fs');

req({ method: 'GET', uri: process.argv[2] }, 'utf-8', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.appendFile(process.argv[3], body, 'utf-8', error => error ? console.log(error) : '');
});
