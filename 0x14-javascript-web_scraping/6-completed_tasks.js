#!/usr/bin/node

const req = require('request');

req(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  let results = JSON.parse(body);
  let userdict = {};
  for (let i = 1; i <= 10; i++) {
    let count = 0;
    for (let j = 0; j < results.length; j++) {
      if (results[j].userId === i) {
        if (results[j].completed === true) {
          count++;
        }
      }
    }
    userdict[i] = count;
  }
  console.log(userdict);
});
