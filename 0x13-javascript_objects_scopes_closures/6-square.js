#!/usr/bin/node
// class Square that defines a square and inherits from 5-square.js

const lastSquare = require('./5-square');

module.exports = class Square extends lastSquare {
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
};
