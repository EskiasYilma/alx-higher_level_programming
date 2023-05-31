/* global $ */
'use strict';

$(document).ready(function () {
  let items = 0;
  $('.my_list').empty();
  $('#add_item').click(function () {
    items += 1;
    $('.my_list').append('<LI>Item</LI>');
  });
  $('#remove_item').click(function () {
    items -= 1;
    $('.my_list li').eq(items).remove();
  });
  $('#clear_list').click(function () {
    items = 0;
    $('.my_list').empty();
  });
});
