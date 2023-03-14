#!/usr/bin/node
// Script prints a square

const squareSize = process.argv[2];

if (!parseInt(squareSize)) {
  console.log('Missing size');
} else {
  for (let counter = 0; counter < squareSize; counter++) {
    let column = 0;
    let line = '';

    while (column < squareSize) {
      line += 'X';
      column++;
    }
    console.log(line);
  }
}
