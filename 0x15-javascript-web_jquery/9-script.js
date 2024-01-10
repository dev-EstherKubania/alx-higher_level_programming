$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Fetch data from the provided URL
    const helloTranslation = data.hello;

    // Update the text of the <div> with the ID "hello"
    $('#hello').text(helloTranslation);
  });
});
