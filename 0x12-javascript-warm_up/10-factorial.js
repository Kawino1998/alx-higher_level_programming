#!/usr/bin/node
function fact (num) {
  if (num === 1) {
    return num;
  }
  return num * fact(num - 1);
}
const num = parseInt(process.argv[2]);
if (isNaN(num) || num === 1) {
  console.log(1);
} else {
  console.log(fact(num));
}
