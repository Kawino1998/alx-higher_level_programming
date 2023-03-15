#!/usr/bin/node
const fs = require('fs');
const str1 = fs.readFileSync(process.argv[2], 'utf8');
const str2 = fs.readFileSync(process.argv[3], 'utf8');
fs.appendFile(process.argv[4], str1, (err) => {
  if (err) throw err;
});
fs.appendFile(process.argv[4], str2, (err) => {
  if (err) throw err;
});
