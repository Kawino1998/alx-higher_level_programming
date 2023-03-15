#!/usr/bin/node
exports.logMe = function (item) {
  const str = exports.logMe.count + ': ' + item;
  console.log(str);
  exports.logMe.count++;
};
exports.logMe.count = 0;
