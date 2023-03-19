#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    const arr = [];
    for (let i = this.width; i > 0; i--) {
      if (c === undefined) {
        arr.push('X');
      } else {
        arr.push(c);
      }
    }
    for (let i = this.height; i > 0; i--) {
      console.log(arr.join(''));
    }
  }
}

module.exports = Square;
