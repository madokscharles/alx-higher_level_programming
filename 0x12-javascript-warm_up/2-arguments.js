#!/usr/bin/node
// Script prints a message depending on number of arguments passed

// Printing value for process.argv
const myArgs = process.argv.length;

if (myArgs > 2) {
  console.log('Argument' + (myArgs > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
