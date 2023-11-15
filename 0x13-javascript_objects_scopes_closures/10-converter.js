#!/usr/bin/node

exports.converter = function (base) {
  function newnumber (number) {
    return number.toString(base);
  }

  return newnumber;
};
