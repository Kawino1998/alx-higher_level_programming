#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const array = [];
  for (let i = process.argv[2]; i > 0; i--) {
    array.push('X');
  }
  for (let i = array.length; i > 0; i--) {
    console.log(array.join(''));
  }
}
