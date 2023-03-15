#!/usr/bin/node
class Rectangle {
    constructor(w, h){
        if (w || h > 0) {
            this.width = w;
            this.height = h;
        } else {
            this.width = null;
            this.height = null;
        }
    }
}
module.exports = Rectangle;
