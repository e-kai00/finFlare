
// Checkbox marked before closing button will be available
document.getElementById('confirmationCheckbox').addEventListener('change', function () {
    const closeAccountBtn = document.getElementById('closeAccountBtn');
    closeAccountBtn.disabled = !this.checked;
    closeAccountBtn.classList.toggle('disabled', !this.checked);
});
