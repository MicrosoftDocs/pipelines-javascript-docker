// Modules
const http = require('http');
const fs = require('fs');

// Server configuration
const hostname = '0.0.0.0';
const port = 80;

// Render page
fs.readFile('./index.html', function (err, html) {
    if (err) {
        throw err; 
    }       
    const server = http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    }).listen(port, hostname, () => {
    	// Console
	  	console.log(`Server running at http://${hostname}:${port}/`);
	});
});