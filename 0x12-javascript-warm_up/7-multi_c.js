#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = process.argv[2]; i > 0; i--) {
    console.log('C is fun');
  }
}
