#!/usr/bin/node
const args = process.argv.slice(2);
const secondBiggest = args.length < 2 ? 0 : args.sort((a, b) => b - a)[1];

console.log(secondBiggest);
