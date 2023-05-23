#!/usr/bin/node

const req = require('request');
let count = 0;

req(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const results = JSON.parse(body).results;
  for (let i = 0; i < results.length; i++) {
    if (results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
