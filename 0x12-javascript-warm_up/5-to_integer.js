#!/usr/bin/node
// Script prints if the first argument can be converted to integer

console.log(parseInt(process.argv[2]) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number');
