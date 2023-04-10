#!/usr/bin/node

/*
increments and calls a function.
*/

module.exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
