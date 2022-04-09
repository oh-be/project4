const amountInput = document.getElementById('amount-input')
const interestRateInput = document.getElementById('interest-rate-input')
const lengthOfLoanInput = document.getElementById('length-of-loan-input')
const calculateBtn = document.getElementById('calculate-btn')
const resetBtn = document.getElementById('reset-btn')
const mortgageFinalResult = document.getElementById('mortgage-final-result')

const errorMessage = 'There is an error in the form, please check it! 😥'
const successMessage = '🧮 Your monthly mortgage payment will be: '

amountInput.addEventListener('focusout',function(e){
    if (!amountInput.validity.valid) {
      amountInput.classList.add('error')
    } else {
        amountInput.classList.remove('error');
    }
})
interestRateInput.addEventListener('focusout',function(e){
    if (!interestRateInput.validity.valid) {
        interestRateInput.classList.add('error')
    } else {
        interestRateInput.classList.remove('error');
    }
})
lengthOfLoanInput.addEventListener('focusout',function(e){
    if (!lengthOfLoanInput.validity.valid) {
        lengthOfLoanInput.classList.add('error')
    } else {
        lengthOfLoanInput.classList.remove('error');
    }
})

calculateBtn.addEventListener('click', function(e){
    if (amountInput.validity.valid && interestRateInput.validity.valid && lengthOfLoanInput.validity.valid) {
        calculateMortgagePayment()
    } else {
        mortgageFinalResult.textContent = errorMessage
        mortgageFinalResult.classList.add('error-message')
        calculateBtn.classList.add('form-error')
        if (!amountInput.validity.valid) {
            amountInput.classList.add('error')
        }
        if (!interestRateInput.validity.valid) {
            interestRateInput.classList.add('error')
        }
        if (!lengthOfLoanInput.validity.valid) {
            lengthOfLoanInput.classList.add('error')
        }
    }
})

function calculateMortgagePayment() {    
    const borrowedMoney = amountInput.value
    const lengthOfLoan = lengthOfLoanInput.value * 12
    const interestRate = interestRateInput.value // Interés en bruto, sin preparar
    const calculedInterest = interestRate / 100 // Lo dividimos por 100
    const interesPreparado = calculedInterest / 12 // Y lo dividimos por 12 para prepararlo

    const percentage = interesPreparado; // 0.065 / 12 = 6.5% / 12
    const percentagePlusOne = interesPreparado + 1
    const exponentiationOperator = (percentagePlusOne ** lengthOfLoan)
    const firstDividend = percentage * exponentiationOperator;
    const secondDividend = exponentiationOperator - 1
    const division = firstDividend / secondDividend
    const mortgage = borrowedMoney
    const quotas = mortgage * division

    console.log('Parte de arriba de la división: ' + firstDividend)
    console.log('Parte de abajo de la división: ' + secondDividend)
    console.log('División: ' + division)
    console.log('A pagar: ' + quotas)

    mortgageFinalResult.textContent = successMessage + quotas.toFixed(2)
    mortgageFinalResult.classList.add('success-message')
    calculateBtn.classList.add('form-success')
    calculateBtn.setAttribute('disabled','disabled')
    resetBtn.style.display = 'block'
}

resetBtn.addEventListener('click', function() {
    resetBtn.style.display = 'none'
    mortgageFinalResult.textContent = ''
    calculateBtn.removeAttribute('disabled')
    calculateBtn.classList.remove('form-success')
})
