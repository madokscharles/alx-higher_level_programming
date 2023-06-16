#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

const file1 = fs.readFileSync(argv[2], 'utf8');
const file2 = fs.readFileSync(argv[3], 'utf8');

const file3 = file1 + file2;
fs.writeFile(argv[4], file3, function (err) {
  if (err) {
    return console.log(err);
  }
});
