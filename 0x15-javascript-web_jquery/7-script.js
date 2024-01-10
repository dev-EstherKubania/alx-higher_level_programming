$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Fetch data from the provided URL
    const characterName = data.name;

    // Update the text of the <div> with the ID "character"
    $('#character').text(characterName);
  });
});
