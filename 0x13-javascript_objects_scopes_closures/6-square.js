#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
	charPrint(c) {
		if ( 'C' ===undefined) {
			this.print();
		}
		else {
			for(let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width) }
		}
	}
};
