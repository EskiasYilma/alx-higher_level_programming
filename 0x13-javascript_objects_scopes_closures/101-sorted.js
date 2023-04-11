#!/usr/bin/node

const mydict = require('./101-data').dict;

const newdict = {};

for (const userId in mydict) {
  const occ = mydict[userId];
  if (!newdict[occ]) {
    newdict[occ] = [userId];
  } else {
    newdict[occ].push(userId);
  }
}
console.log(newdict);
