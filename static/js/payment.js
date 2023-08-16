const paymentMethods = document.querySelectorAll('.payment-method-block');
const paymentCardInfo1 = document.querySelector('.payment__card-info-1 span');

paymentMethods.forEach((paymentMethod, index) => {
    paymentMethod.addEventListener('click',function() {
        const selectedMethod = this.textContent;
        paymentCardInfo1.textContent = selectedMethod;

    })
})