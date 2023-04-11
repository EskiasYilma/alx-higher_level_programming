#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const f1 = fs.readFileSync(fileA, 'utf8');
const f2 = fs.readFileSync(fileB, 'utf8');
const f3 = f1 + f2;

fs.writeFileSync(fileC, f3);
