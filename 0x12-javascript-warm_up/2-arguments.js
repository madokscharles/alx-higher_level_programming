#!/usr/bin/node
// Script prints a message depending on number of arguments passed

// Importing the process module
const process = require('process');

// Printing value for process.argv
const myArgs = process.argv;

if (myArgs.length === 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
