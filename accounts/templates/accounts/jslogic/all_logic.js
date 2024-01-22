const stockPrices = {
    apple: 200.00,
    xrp: 0.55,
    bitcoin: 41755.30
};

// Update account balance and stock balances
function updateBalances() {
    const accountBalance = parseFloat(localStorage.getItem('accountBalance')) || 0;
    const userStocks = JSON.parse(localStorage.getItem('userStocks')) || {};

    if (accountBalance === 0 && Object.keys(userStocks).length === 0) {
        handleResetClick();
    }

    document.getElementById('account-balance').textContent = accountBalance.toFixed(2);
    updateStockBalances(userStocks);
}

// Handle buy button click
function handleBuyClick(event) {
    const buttonText = event.target.textContent.trim();
    if (buttonText !== "Buy") return;

    const li = event.target.closest('li');
    const stockName = li.childNodes[0].textContent.trim().toLowerCase();
    const input = li.querySelector('input[type="text"]');
    const quantityString = input.value.replace(/,/g, '');
    const quantity = parseFloat(quantityString);
    const stockPriceElement = li.querySelector('.stock-price');
    const price = parseFloat(stockPriceElement.textContent.replace('$', '').replace(',', ''));

    if (isNaN(quantity) || quantity <= 0) {
        alert("Please enter a valid quantity to buy.");
        return;
    }

    const cost = quantity * price;
    let accountBalance = parseFloat(localStorage.getItem('accountBalance') || '10000');
    let userStocks = JSON.parse(localStorage.getItem('userStocks')) || {};

    if (accountBalance >= cost) {
        if (confirm(`You are about to buy ${quantity} of ${stockName.toUpperCase()} stock(s) for $${cost.toFixed(2)}. Do you want to proceed?`)) {
            accountBalance -= cost;
            userStocks[stockName] = (userStocks[stockName] || 0) + quantity;

            localStorage.setItem('accountBalance', accountBalance.toString());
            localStorage.setItem('userStocks', JSON.stringify(userStocks));

            updateBalances();
            clearInputField(event);
        }
    } else {
        alert('Insufficient funds to complete this purchase.');
    }
}

function clearInputField(event) {
    const input = event.target.closest('li').querySelector('input[type="text"]');
    input.value = '';
}

// Handle sell button click
function handleSellClick(event) {
    const buttonText = event.target.textContent.trim();
    if (buttonText !== "Sell") return;

    const li = event.target.closest('li');
    const stockName = li.childNodes[0].textContent.trim().toLowerCase();
    const input = li.querySelector('input[type="text"]');
    const quantityToSellString = input.value.replace(/,/g, '');
    const quantityToSell = parseFloat(quantityToSellString);
    const stockPriceElement = li.querySelector('.stock-price');
    const price = parseFloat(stockPriceElement.textContent.replace('$', '').replace(',', ''));

    if (isNaN(quantityToSell) || quantityToSell <= 0) {
        alert("Please enter a valid quantity to sell.");
        return;
    }

    let userStocks = JSON.parse(localStorage.getItem('userStocks')) || {};

    if (userStocks[stockName] && userStocks[stockName] >= quantityToSell) {
        const saleValue = price * quantityToSell;

        if (confirm(`You are about to sell ${quantityToSell} of ${stockName.toUpperCase()} stock(s) for $${saleValue.toFixed(2)}. Do you want to proceed?`)) {
            userStocks[stockName] -= quantityToSell;

            if (userStocks[stockName] === 0) {
                delete userStocks[stockName];
            }

            let accountBalance = parseFloat(localStorage.getItem('accountBalance') || '10000');
            accountBalance += saleValue;

            localStorage.setItem('accountBalance', accountBalance.toString());
            localStorage.setItem('userStocks', JSON.stringify(userStocks));

            document.getElementById('account-balance').textContent = accountBalance.toFixed(2);
            updateStockBalances(userStocks);
            input.value = '';
        }
    } else {
        alert('You do not own sufficient stocks to sell the specified quantity.');
    }
}

// Handle reset button click
function handleResetClick() {
    // Confirm with the user before resetting account and stock balance
    if (confirm('Are you sure you want to reset your account balance and stock balance to their initial values?')) {
        // Reset the account balance to its initial value
        localStorage.setItem('accountBalance', '10000');

        // Reset the stock balance to its initial value
        localStorage.setItem('userStocks', JSON.stringify({}));

        updateBalances();
    }
}

// Update stock balance display
function updateStockBalances(userStocks) {
    const stockBalanceElement = document.getElementById('stock-balance');
    let totalStockBalanceValue = 0;

    for (const [stock, quantity] of Object.entries(userStocks)) {
        totalStockBalanceValue += quantity * (stockPrices[stock.toLowerCase()] || 0);
    }

    stockBalanceElement.textContent = `${totalStockBalanceValue.toFixed(2)}`;

    if (totalStockBalanceValue === 0) {
        stockBalanceElement.textContent = '0.00';
    }
}

// Update total balance display
function updateTotalBalance() {
    const accountBalance = parseFloat(localStorage.getItem('accountBalance') || '10000');
    const stockBalance = parseFloat(document.getElementById('stock-balance').textContent.replace('$', '').replace(',', ''));

    const totalBalance = accountBalance + stockBalance;
    document.getElementById('total').textContent = `${totalBalance.toFixed(2)}`;
}

// Initialize event listeners
document.addEventListener('DOMContentLoaded', function () {
    updateBalances();

    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', (event) => {
            if (event.target.textContent.trim() === "Buy") {
                handleBuyClick(event);
            } else if (event.target.textContent.trim() === "Sell") {
                handleSellClick(event);
            }
            updateTotalBalance();
            clearInputField(event);
        });
    });

    document.getElementById('reset').addEventListener('click', handleResetClick);
});