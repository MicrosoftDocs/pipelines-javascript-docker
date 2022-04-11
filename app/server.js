'use strict';

const express = require('express');

const PORT = 8080;
const HOST = '0.0.0.0';

function fibo(n) { 

  console.log("N is:" + n)
  if (n < 2)
      return 1;
  else   return fibo(n - 2) + fibo(n - 1);
}


const app = express();
app.get('/', (req, res) => {
  let num = parseInt(req.headers.fibo); 
  console.log(num)
  res.send('Hello world ' + num);
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);