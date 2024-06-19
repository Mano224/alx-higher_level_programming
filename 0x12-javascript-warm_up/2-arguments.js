#!/usr/bin/node
<<<<<<< HEAD
/* learning how to pass arguments*/
if (process.argv.length === 2){
        console.log('No argument');
}
else if (process.argv.length === 3){
        console.log('Argument found');
}
else {
        console.log('Arguments found');
}
=======
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
>>>>>>> 240a82c820c6623aef953ef2de010de5f35520e1

