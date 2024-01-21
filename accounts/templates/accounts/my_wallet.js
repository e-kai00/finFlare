document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', (event) => {
      const buttonText = event.target.textContent.trim();
      if(buttonText === "Buy") {
        const li = event.target.closest('li');
        const stockName = li.childNodes[0].textContent.trim().toLowerCase();
        const input = li.querySelector('input[type="text"]');
        const quantity = parseFloat(input.value);
        const stockPriceElement = li.querySelector('.stock-price');
        const price = parseFloat(stockPriceElement.textContent.replace('$', '').replace(',', ''));
  
        if(isNaN(quantity) || quantity <= 0) {
          alert("Please enter a valid quantity to buy.");
          return;
        }
  
        // Get the current stock price from the stockPrices object
        const cost = quantity * price;
        
        // Then fetch and update account balance and user stocks from localStorage
        let accountBalance = parseFloat(localStorage.getItem('accountBalance') || '10000');
           // ...continuing from existing code
        let userStocks = JSON.parse(localStorage.getItem('userStocks')) || {};
  
        // Check if enough funds to purchase stocks
        if (accountBalance >= cost) {
          accountBalance -= cost;
          userStocks[stockName] = (userStocks[stockName] || 0) + quantity;
  
          // Update the localStorage with the new account balance and userStocks
          localStorage.setItem('accountBalance', accountBalance.toString());
          localStorage.setItem('userStocks', JSON.stringify(userStocks));
  
          // Update balances displayed on the page
          updateBalances();
        } else {
          alert('Insufficient funds to complete this purchase.');
        }
      }
    });
  });
  
  const stockPrices = {
    'apple': 200.00,
    'xrp': 0.55,
    'bitcoin': 41755.30
  };
  
  function updateBalances() {
    let accountBalanceElement = document.getElementById('account-balance');
    let stockBalanceElement = document.getElementById('stock-balance');
  
    // Retrieve balances from localStorage
    let accountBalance = parseFloat(localStorage.getItem('accountBalance') || '10000');
    let userStocks = JSON.parse(localStorage.getItem('userStocks')) || {};
  
    accountBalanceElement.textContent = `$${accountBalance.toFixed(2)}`;
  
    let totalStockValue = 0;
    for (const [stock, quantity] of Object.entries(userStocks)) {
  const stockPrice = stockPrices[stock.toLowerCase()] || 0;
  totalStockValue += stockPrice * quantity;
    }
  stockBalanceElement.textContent = `$${totalStockValue.toFixed(2)}`;
  }
  
  // Call updateBalances on DOMContentLoaded to ensure the page is fully loaded
  document.addEventListener('DOMContentLoaded', updateBalances);