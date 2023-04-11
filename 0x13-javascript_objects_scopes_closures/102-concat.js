#!/usr/bin/node

const fs = require('fs');

const f1 = fs.readFileSync('fileA', 'utf8');
const f2 = fs.readFileSync('fileB', 'utf8');
const f3 = f1 + f2;

fs.writeFileSync('fileC', f3);
