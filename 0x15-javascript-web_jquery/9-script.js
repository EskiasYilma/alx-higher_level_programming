/* global $ */
'use strict';

const settings = {
  async: true,
  crossDomain: true,
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  headers: {
    Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    DNT: '1',
    Connection: 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site'
  }
};

$.ajax(settings).done(function (response) {
  const hello = response.hello;
  $('#hello').text(hello);
  console.log(response);
});
