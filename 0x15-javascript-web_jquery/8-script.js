$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Fetch data from the provided URL
    const movies = data.results;

    // Loop through the list of movies and append titles to the UL#list_movies
    for (const movie of movies) {
      $('<li>').text(movie.title).appendTo('#list_movies');
    }
  });
});
