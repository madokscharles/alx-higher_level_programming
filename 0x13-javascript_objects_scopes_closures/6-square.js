#!/usr/bin/node
/**
 * class Square that defines a square and inherits from Square of 5-square.js
 */

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    let myVar = '';
    for (let i = 0; i < this.width; i++) {
      myVar += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(myVar);
    }
  }
}

module.exports = Square;
