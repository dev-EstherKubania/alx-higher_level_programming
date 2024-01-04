#!/usr/bin/node

const fileName = process.argv[2];
const fs = require('fs');

fs.readFile(fileName, 'utf-8', (errr, data) => {
  if (errr) {
    console.error(errr);
  } else {
    console.log(data);
  }
});
