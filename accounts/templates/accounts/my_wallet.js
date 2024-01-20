document.getElementById('depositButton').addEventListener('click', function() {
    const depositAmountInput = document.getElementById('depositAmount');
    const depositAmount = parseFloat(depositAmountInput.value);
    
    if (isNaN(depositAmount)) {
        alert('Please enter a valid deposit amount.');
        return;
    }

    const currentBalance = parseFloat(document.getElementById('accountBalance').textContent);
    const newBalance = (currentBalance + depositAmount).toFixed(2);

    document.getElementById('accountBalance').textContent = newBalance;
});