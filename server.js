 /*
const ngrok = require('ngrok');
const express = require('express')

let endpoint = ''
const app = express();

app.get('/', (req, res) => res.redirect('https://skywalkingzulu.github.io/Taxitv/primeframe.html'))

const server = app.listen(9088, () => {
 
  ngrok.connect(9088).then(ngrokUrl => {
    endpoint = ngrokUrl
    console.log(`Verification Service running, open at ${endpoint}`)
  })
 
})
 */
var express = require('express');

var app = express();

app.get('/', function(req, res){
  res.redirect('https://skywalkingzulu.github.io/Taxitv/primeframe.html');
});

/* istanbul ignore next */
if (!module.parent) {
  app.listen(3000);
  console.log('Express started on port 3000');
}

