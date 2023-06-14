#!/usr/bin/node
const first = process.argv[2];
const second = process.argv[3];

function add (first, second) {
  return (first + second);
}

console.log(add(parseInt(first), parseInt(second)));
