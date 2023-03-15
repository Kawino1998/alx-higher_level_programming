#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    const arr = [];
    for (let col = this.width; col > 0; col--) {
      arr.push('X');
    }
    for (let row = this.height; row > 0; row--) {
      console.log(arr.join(''));
    }
  }
}
module.exports = Rectangle;
