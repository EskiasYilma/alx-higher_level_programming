#!/usr/bin/node

const oldlist = require('./100-data').list;

const newlist = oldlist.map((val, idx) => val * idx);
console.log(oldlist);
console.log(newlist);
