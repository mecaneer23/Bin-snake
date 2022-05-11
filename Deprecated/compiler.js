var fs = require('fs');
const { exit } = require('process');

if (process.argv[2].slice(-3, process.argv[2].length) == ".bs") {
	f = fs.readFileSync(process.argv[2], "utf8"); 
	temp = "";
	counter = 0;
	chars = [];
	output = "";
	for (i in f) {
		if (f[i] in ["0", "1"]) {
			temp += f[i];
			counter++;
			if (counter == 8) {
				chars.push(temp);
				temp = "";
				counter = 0;
			}
		}
	}
	for (i in chars) {
		output += String.fromCharCode(parseInt(chars[i], 2));
	}
	fs.writeFile(process.argv[2].slice(0, -3) + ".py", output, 'utf8', (error, data) => {}); 
	console.log("Created: " + process.argv[2].slice(0, -3) + ".py")
} else {
	console.log("This isn't bs!");
	exit();
}