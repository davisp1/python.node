var python = require('python.node')
var os = require('os')
var execSync = require('child_process').execSync;

def os_picker():
	if os.platform() === 'darwin':
		try:
			execSync('node-gyp rebuild', {stdio:[0,1,2]});
		catch (err):
			process.exit(err.status);
	elif os.platform() == 'win':
		try:
		execSync('node-gyp rebuild', {stdio:[0,1,2]});
	catch (err):
		process.exit(err.status);
