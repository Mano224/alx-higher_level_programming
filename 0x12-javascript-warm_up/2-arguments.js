#!/usr/bin/node
function printMessage(args) {
    if (args.length === 0) {
        console.log("No argument");
    } else if (args.length === 1) {
        console.log("Argument found");
    } else {
        console.log("Arguments found");
    }
}

// Example usage
const args = process.argv.slice(2);
printMessage(args);

