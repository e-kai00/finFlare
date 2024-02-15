// Update account balance and stock balances
function updateWalletBalances() {
    let accountBalance; // Declare accountBalance outside the fetch callback

    // Fetch account balance from Django
    fetch('/get_user_balance/')
        .then(response => response.json())
        .then(data => {
            accountBalance = data.balance;
            document.getElementById('account-balance').textContent = accountBalance.toFixed(4);

            if (accountBalance === 0 && Object.keys(userStocks).length === 0) {
                handleResetClick();
            }

            document.getElementById('account-balance').textContent = accountBalance.toFixed(2);
            updateStockBalances(userStocks);

            // Update stock balance element
            document.getElementById('stock-balance').textContent = totalStockBalanceValue.toFixed(2);
        });
}

function getCsrfToken() {
    const csrfTokenElement = document.getElementsByName('csrfmiddlewaretoken')[0];
    return csrfTokenElement.value;
}


// Fetch stock prices from Django
fetch('/get_stock_prices/')
    .then(response => response.json())
    .then(stockPrices => {
        updateStockPrices(stockPrices);
    });

// Add this function to update stockPrices
function updateStockPrices(newStockPrices) {
    stockPrices = newStockPrices;
    // Optionally, you can update the displayed stock prices on the UI
    // For example, if you have HTML elements displaying stock prices, update them here
}

fetch('/get_user_stock_balances/')
    .then(response => response.json())
    .then(userStockBalances => {
        updateStockBalance(userStockBalances);
    });

// Handle buy button click
function handleBuyClick(event) {
    const buttonText = event.target.textContent.trim();
    if (buttonText !== "Buy") return;

    const li = event.target.closest('li');
    const stockName = li.childNodes[0].textContent.trim().toLowerCase();
    const input = li.querySelector('input[type="text"]');
    const quantityString = input.value.replace(/,/g, '');
    const quantity = parseFloat(quantityString);

    const csrfToken = getCsrfToken();

    fetch('/buy_stock/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            stockName: stockName,
            quantity: quantity,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response, you might want to show a success or error message
        console.log(data);
        updateBalances(); // Update balances after buying
    });

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

    const csrfToken = getCsrfToken();

    fetch('/sell_stock/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            stockName: stockName,
            quantityToSell: quantityToSell,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response, you might want to show a success or error message
        console.log(data);
        updateBalances(); // Update balances after selling
    });

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


// Add this function to update user stock balances
function updateUserStockBalances(userStockBalances) {
    // You might want to update the UI to reflect the user's stock balances
    // For example, if you have HTML elements displaying stock balances, update them here
    const stockBalanceElement = document.getElementById('stock-balance');
    let totalStockBalanceValue = 0;

    for (const [stock, balanceData] of Object.entries(userStockBalances)) {
        totalStockBalanceValue += balanceData.purchase_price * balanceData.quantity;
        // Update other UI elements based on userStockBalances if needed
    }

    stockBalanceElement.textContent = `${totalStockBalanceValue.toFixed(2)}`;
}

// Update stock balance
function updateStockBalance(userStockBalances) {
    // Calculate the total value of stocks the user has purchased
    // You might want to update the UI to reflect the user's stock balances
    // For example, if you have HTML elements displaying stock balances, update them here
    const stockBalanceElement = document.getElementById('stock-balance');
    let totalStockBalanceValue = 0;

    for (const [stock, balanceData] of Object.entries(userStockBalances)) {
        totalStockBalanceValue += balanceData.purchase_price * balanceData.quantity;
        // Update other UI elements based on userStockBalances if needed
    }

    stockBalanceElement.textContent = `${totalStockBalanceValue.toFixed(2)}`;
}

// Call the updated function when the page loads
document.addEventListener('DOMContentLoaded', function () {
    // Call the appropriate initialization function
    updateWalletBalances();

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

fetch('/get_total_balance/')
    .then(response => response.json())
    .then(data => {
        const totalBalance = data.total_balance;
        document.getElementById('total').textContent = totalBalance.toFixed(2);
    });


// Initialize event listeners and call the appropriate initialization function
document.addEventListener('DOMContentLoaded', function () {
    updateWalletBalances();

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

// Fetch total balance
fetch('/get_total_balance/')
    .then(response => response.json())
    .then(data => {
        const totalBalance = data.total_balance;
        document.getElementById('total').textContent = totalBalance.toFixed(2);
    });