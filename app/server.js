'use strict';

const express = require('express');

const PORT = 80;
const HOST = '0.0.0.0';

const app = express();
let http = require('http');
let fs = require('fs');
 
let handleRequest = (request, response) => {
    response.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    fs.readFile('./index.html', null, function (error, data) {
        if (error) {
            response.writeHead(404);
            respone.write('file not found');
        } else {
            response.write(data);
        }
        response.end();
    });
};
console.log(`Running on http://${HOST}:${PORT}`);
