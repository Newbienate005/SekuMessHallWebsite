// Function to show the signup form
function showSignup() {
    document.getElementById("login-form").style.display = "none";
    document.getElementById("signup-form").style.display = "block";
}

// Function to show the login form
function showLogin() {
    document.getElementById("signup-form").style.display = "none";
    document.getElementById("login-form").style.display = "block";
}

// Function to update signup fields based on role selection
function updateSignupFields() {
    const role = document.getElementById("signup-role").value;
    const usernameField = document.getElementById("signup-username");
    const regNumberField = document.getElementById("signup-registration");
    const passwordField = document.getElementById("signup-password");
    const signupButton = document.querySelector("#signup-form button");

    // Initially hide all fields
    usernameField.style.display = "none";
    regNumberField.style.display = "none";
    passwordField.style.display = "none";
    signupButton.style.display = "none";

    if (role) {
        usernameField.style.display = "block";
        passwordField.style.display = "block";
        signupButton.style.display = "block";

        if (role === "student") {
            regNumberField.style.display = "block"; // Show registration number for students
        }
    }
}

// Function to sign up a user
function signup() {
    const role = document.getElementById("signup-role").value;
    const username = document.getElementById("signup-username").value;
    const registrationNumber = document.getElementById("signup-registration").value;
    const password = document.getElementById("signup-password").value;

    // Ensure required fields are filled
    if (!role || !username || !password || (role === "student" && !registrationNumber)) {
        alert("Please fill all required fields.");
        return;
    }

    // Validate student registration number format
    if (role === "student") {
        const regPattern = /^G\d{3}\/\d{4}\/\d{4}$/;
        if (!regPattern.test(registrationNumber)) {
            alert("Invalid registration number format. Use G127/1448/2023.");
            return;
        }
    }

    // Prepare form data
    let formData = new FormData();
    formData.append("role", role);
    formData.append("username", username);
    formData.append("password", password);
    if (role === "student") {
        formData.append("registration_number", registrationNumber);
    }

    // Send signup request
    fetch("/signup/", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": getCSRFToken(),
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Signup successful") {
            alert("Signup successful! Redirecting...");
            window.location.href = "/index/";  // Redirect to index.html
        } else {
            alert("Signup failed: " + data.error);
        }
    })
    .catch(error => console.error("Error:", error));
}

// Function to get CSRF token (important for Django)
function getCSRFToken() {
    let csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken'))?.split('=')[1];
    if (!csrfToken) {
        console.error("CSRF token not found! Ensure your template includes {% csrf_token %}.");
    }
    return csrfToken;
}
