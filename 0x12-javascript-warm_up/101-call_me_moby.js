#!/usr/bin/node

/*
returns the addition of 2 integers.
*/

module.exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
