// Implement the sell button
document.querySelectorAll('.btn').forEach(button => {
    // Targeting the text "Sell" in the sell buttons
    if (button.textContent.trim() === 'Sell') {
        button.addEventListener('click', () => {
         // Get the user input
    const stockId = document.getElementById('stock-id').value;
    const quantity = parseInt(document.getElementById('quantity').value);
    // Check if the user has enough stocks in their stock balance
    const userStocks = JSON.parse(localStorage.getItem('userStocks')) || [];
    const stockIndex = userStocks.findIndex(stock => stock.stockId === stockId);
    if (stockIndex !== -1 && userStocks[stockIndex].quantity >= quantity) {
      // Add the proceeds from the sale to the account balance
    const stockPrice = 50; // Replace this with the actual stock price
    const proceeds = stockPrice * quantity;
    const accountBalance = parseFloat(document.getElementById('account-balance').textContent.replace('$', '')) + proceeds;
document.getElementById('account-balance').textContent = `$${accountBalance.toFixed(2)}`;
      // Deduct the sold stocks from the user's stock balance
    userStocks.splice(stockIndex, 1);
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