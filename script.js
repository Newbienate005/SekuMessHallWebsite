let cart = [];
let total = 0;

document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', () => {
    const item = button.parentElement;
    const itemName = item.getAttribute('data-name');
    const itemPrice = parseFloat(item.getAttribute('data-price'));

    cart.push({ name: itemName, price: itemPrice });
    total += itemPrice;

    updateCart();

    document.getElementById('checkout').style.display = 'block';
    document.getElementById('pay-now').style.display = 'block';
  });
});

function updateCart() {
  const cartItems = document.getElementById('cart-items');
  const totalElement = document.getElementById('total');

  cartItems.innerHTML = '';

  cart.forEach(item => {
    const li = document.createElement('li');
    li.textContent = `${item.name} - $${item.price}`;
    cartItems.appendChild(li);
  });

  totalElement.textContent = total.toFixed(2);
}

document.getElementById('checkout').addEventListener('click', () => {
  const phoneNumber = prompt("Enter your M-Pesa phone number (e.g., 2547XXXXXXXX):");

  if (phoneNumber) {
    if (/^2547\d{8}$/.test(phoneNumber)) { 
      alert(`Payment request sent to ${phoneNumber}. Please check your phone to complete the payment.`);
      setTimeout(() => {
        alert(`Payment of $${total.toFixed(2)} successful! Click "Pay Now" to generate your receipt.`);
      }, 3000);
    } else {
      alert("Invalid phone number. Please enter a valid M-Pesa number (e.g., 2547XXXXXXXX).");
    }
  } else {
    alert("Payment canceled. Please try again.");
  }
});

document.getElementById('pay-now').addEventListener('click', () => {

  localStorage.setItem('cart', JSON.stringify(cart));
  localStorage.setItem('total', total.toFixed(2));

  window.location.href = 'receipt.html';
});