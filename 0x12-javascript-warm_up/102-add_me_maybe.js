#!/usr/bin/node

/*
executes x times a function.
*/

module.exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
