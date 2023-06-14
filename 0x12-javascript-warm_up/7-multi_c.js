#!/usr/bin/node
const args = process.argv[2];

if (isNaN(parseInt(+args))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(+args); i++) {
    console.log('C is fun');
  }
}
