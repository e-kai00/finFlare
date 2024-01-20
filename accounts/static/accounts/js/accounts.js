// Select all elements with the class .balance-numbers
var balanceNumbers = document.querySelectorAll('.balance-numbers');

// Iterate over the selected elements
balanceNumbers.forEach(function(element) {
  // Parse the content of the element as a float
  var value = parseFloat(element.textContent);

  // If the value is less than 0, change the color
  if (value < 0) {
    element.style.color = 'var(--accent-color-2)';
  }
});