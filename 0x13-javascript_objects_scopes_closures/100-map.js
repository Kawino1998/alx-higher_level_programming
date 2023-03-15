#!/usr/bin/node
const list = require('./100-data').list;
const map1 = list.map(function (currentValue, index) { return currentValue * index; });
console.log(list);
console.log(map1);
