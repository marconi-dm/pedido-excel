document.addEventListener('DOMContentLoaded', () => {
    const errorMessage = document.querySelector('.error-message');
    const submitButton = document.querySelector('input[type="submit"]');
    const form = document.querySelector('form')

        submitButton.addEventListener('click', (e) => {
            if(errorMessage){
                e.preventDefault();
                // Oculta a mensagem de erro
                errorMessage.style.display = 'none';
                form.submit();
            }
            
            
        });
});
