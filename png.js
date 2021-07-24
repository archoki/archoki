#!/usr/bin/env node

const convert = require('png-to-ico');
const fs = require('fs/promises');

(async function() {
  try {
    const png = await fs.readFile('./assets/logo.png');
    const ico = await convert(png);
    await fs.writeFile('./favicon.ico', new Uint8Array(ico.buffer));
  } catch (e) {
    await fs.appendFile('./log', e);
    console.log('\x1b[01;31merror\x1b[0m: ' + e);
    return process.exit(1);
  }
}).call(this);