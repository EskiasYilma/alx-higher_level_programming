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

  rotate () {
    const w = this.width;
    const h = this.height;
    this.height = w;
    this.width = h;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
