#!/usr/bin/node

const oldlist = require('./100-data').list;

const newlist = oldlist.map(x => x * oldlist.indexOf(x));
console.log(oldlist);
console.log(newlist);
