/* global $ */
'use strict';

$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    const films = data.films;
    films.forEach(function (ttls) {
      $.getJSON(ttls, function (ttlData) {
        const titles = ttlData.title;
        const listItem = $('<li>').text(titles);
        $('#list_movies').append(listItem);
      });
    });
  });
});
