#!/usr/bin/node

const req = require('request');

req('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
