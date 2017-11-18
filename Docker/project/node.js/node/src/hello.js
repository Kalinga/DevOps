var http = require('http');
var PORT = 8081;

//App 
var app = http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello World\n');
	}
  );

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);