#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super();
    if (size <= 0 || typeof size !== 'number') {
      return;
    }
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
