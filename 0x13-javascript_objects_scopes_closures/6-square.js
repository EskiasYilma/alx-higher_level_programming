#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let freq = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        freq += c;
      }
      if (i === this.height - 1) {
        break;
      } else {
        freq += '\n';
      }
    }
    console.log(freq);
  }
}

module.exports = Square;
