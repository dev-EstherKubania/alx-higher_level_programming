$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $('#add_item').click(function () {
    // When the DIV#add_item is clicked, add a new <li> element to UL.my_list
    $('<li>Item</li>').appendTo('.my_list');
  });
});
