'use strict';

const express = require('express');

const PORT = 80;
const HOST = '0.0.0.0';

const app = express();
app.register('.html', require('jade'));

app.get('/', (req, res) => {
  res.render('index.html');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
