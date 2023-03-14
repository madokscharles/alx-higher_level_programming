#!/usr/bin/node
// Script prints a square

const squareSize = process.argv[2];

if (!parseInt(squareSize)) {
  console.log('Missing size');
} else {
  let counter = 1;
  while (counter <= squareSize) {
    let column = 1;
    let line = '';

    while (column <= squareSize) {
      line += 'X';
      column++;
    }
    console.log(line);
    counter++;
  }
}
