#!/usr/bin/node
process = require(args)
if (args.length === 0){
	console.log('No argument');
}
else if (args.length === 1){
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
args = process.argv

