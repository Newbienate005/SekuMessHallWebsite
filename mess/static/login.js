// Show Login Form
function showLogin() {
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('signup-form').style.display = 'none';
}

// Show Signup Form
function showSignup() {
    document.getElementById('signup-form').style.display = 'block';
    document.getElementById('login-form').style.display = 'none';
}

// Update Login Fields Based on Role
function updateLoginFields() {
    const role = document.getElementById('login-role').value;
    const usernameField = document.getElementById('login-username');
    usernameField.placeholder = role === 'student' ? 'Registration Number' : 'Full Name';
}

// Update Signup Fields Based on Role
function updateSignupFields() {
    const role = document.getElementById('signup-role').value;
    const usernameField = document.getElementById('signup-username');
    const registrationField = document.getElementById('signup-registration');
    const passwordField = document.getElementById('signup-password');
    const signupButton = document.querySelector('#signup-form button');

    if (role === 'student') {
        usernameField.style.display = 'none';
        registrationField.style.display = 'block';
        passwordField.style.display = 'block';
        signupButton.style.display = 'block';
    } else if (role === 'worker' || role === 'admin') {
        usernameField.style.display = 'block';
        registrationField.style.display = 'none';
        passwordField.style.display = 'block';
        signupButton.style.display = 'block';
    } else {
        usernameField.style.display = 'none';
        registrationField.style.display = 'none';
        passwordField.style.display = 'none';
        signupButton.style.display = 'none';
    }
}

// Login Functionality
function login() {
    const role = document.getElementById('login-role').value;
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    // Validate Student Registration Number
    if (role === 'student' && !username.match(/^[A-Z]\d{3,4}$/)) {
        alert('Invalid registration number. Format: Uppercase letter followed by 3 or 4 digits.');
        return;
    }

    // Validate Worker/Admin Full Name
    if ((role === 'worker' || role === 'admin') && username.trim() === '') {
        alert('Please enter your full name.');
        return;
    }

    // Validate Password
    if (password.trim() === '') {
        alert('Please enter a password.');
        return;
    }

    // Redirect based on role
    if (role === 'student') {
        window.location.href = 'student.html';
    } else if (role === 'worker') {
        window.location.href = 'worker.html';
    } else if (role === 'admin') {
        window.location.href = 'admin.html';
    }
}

// Signup Functionality
function signup() {
    const role = document.getElementById('signup-role').value;
    const username = document.getElementById('signup-username').value;
    const registration = document.getElementById('signup-registration').value;
    const password = document.getElementById('signup-password').value;

    // Validate Student Registration Number
    if (role === 'student' && !registration.match(/^[A-Z]\d{3,4}$/)) {
        alert('Invalid registration number. Format: Uppercase letter followed by 3 or 4 digits.');
        return;
    }

    // Validate Worker/Admin Full Name
    if ((role === 'worker' || role === 'admin') && username.trim() === '') {
        alert('Please enter your full name.');
        return;
    }

    // Validate Password
    if (password.trim() === '') {
        alert('Please enter a password.');
        return;
    }

    // Corrected Template String for Alert
    alert(`Signed up as ${role}: ${role === 'student' ? registration : username}`);

    // Redirect based on role
    if (role === 'student') {
        window.location.href = "{% url 'index' %}";
    } else if (role === 'worker') {
        window.location.href = "{% url 'index' %}";
    } else if (role === 'admin') {
        window.location.href = "{% url 'index' %}";
    }
}
