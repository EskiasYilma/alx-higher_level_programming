#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || typeof w !== 'number' || h <= 0 || typeof h !== 'number') {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let freq = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        freq += 'X';
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

module.exports = Rectangle;
