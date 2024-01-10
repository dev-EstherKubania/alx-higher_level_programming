$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $('#update_header').click(function () {
    // When the DIV#update_header is clicked, update the text of the <header> element
    $('header').text('New Header!!!');
  });
});
