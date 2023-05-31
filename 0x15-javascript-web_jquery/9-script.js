/* global $ */
'use strict';

$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    const hello = data.hello;
    $('#hello').text(hello);
  });
});
