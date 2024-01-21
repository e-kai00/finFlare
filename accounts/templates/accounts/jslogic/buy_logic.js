
// Implement the buy button
document.querySelectorAll('.btn').forEach(button => {
    // Targeting the text "Buy" in the buy buttons
    if (button.textContent.trim() === 'Buy') {
        button.addEventListener('click', () => {
    // Get the user input
    const stockId = document.getElementById('stock-id').value;
    const quantity = parseInt(document.getElementById('quantity').value);
    // Check if the user has enough funds in their account balance
    if (quantity > 0 && parseFloat(document.getElementById('account-balance').textContent.replace('$', '')) >= 0) {
      // Deduct the cost of the stock from the account balance
      const stockPrice = 0; // Replace this with the actual stock price from...
      const cost = stockPrice * quantity;
    const accountBalance = parseFloat(document.getElementById('account-balance').textContent.replace('$', '')) - cost;
    document.getElementById('account-balance').textContent = `$${accountBalance.toFixed(2)}`;
      // Add the stock to the user's stock balance
    const userStocks = JSON.parse(localStorage.getItem('userStocks')) || [];
        userStocks.push({ stockId, quantity });
        localStorage.setItem('userStocks', JSON.stringify(userStocks));
      // Update the stock balance displayed to the user
    let totalValue = 0;
    for (const stock of userStocks) {
        const stockPrice = data.stocks[stock.stockId].price;
        totalValue += stockPrice * stock.quantity;
    }
    document.getElementById('stock-balance').textContent = `$${totalValue.toFixed(2)}`;
    }
});
    }
});