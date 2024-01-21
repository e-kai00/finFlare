// Implement the reset button
    document.getElementById('reset-button').addEventListener('click', () => {
    // Check if the user has an account balance of 0 and also owns 0 stocks or has a 0 balance and stocks with a negative value
        if (confirm('Are you sure you want to reset your account balance and stock balance to their initial values?')) {
      // Reset the account balance and stock balance to their initial values
    document.getElementById('account-balance').textContent = '$10,000.00';
    document.getElementById('stock-balance').textContent = '$0.00';
    }
});
