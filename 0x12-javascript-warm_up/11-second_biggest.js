#!/usr/bin/node
const len = process.argv.length;
if (process.argv[2] === undefined) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  const array = [];
  for (let i = len; i > 2; i--) {
    array.push(parseInt(process.argv[i - 1]));
  }
  array.sort((left, right) => left - right);
  const secondBiggest = len - 4;
  console.log(array[secondBiggest]);
}
