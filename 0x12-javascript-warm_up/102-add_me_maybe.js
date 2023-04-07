#!/usr/bin/node
// Function increments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
