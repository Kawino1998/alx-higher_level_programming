#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
const values = Object.values(dict);
const setValues = [...new Set(values)];
for (let i = 0; i < setValues.length; i++) {
  newDict[setValues[i]] = [];
}
for (const key in dict) {
  newDict[dict[key]].push(key);
}
console.log(newDict);
