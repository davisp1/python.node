var os = require('os')
var execSync = require('child_process').execSync;


if (os.platform() === 'darwin') {
	try {
		execSync('node-gyp rebuild', {stdio:[0,1,2]});
	} catch (err) {
		process.exit(err.status);
	}
}