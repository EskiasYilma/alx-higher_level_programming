#!/usr/bin/node

const req = require('request');

req('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const results = JSON.parse(body).characters;
  for (let i = 0; i < results.length; i++) {
    req(results[i], (err, resp, bd) => {
      if (err) {
        console.log(err);
      }
      const chars = JSON.parse(bd).name;
      console.log(chars);
    });
  }
});
