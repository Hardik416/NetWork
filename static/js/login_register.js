// Dark mode toggle
const toggle = document.getElementById('darkToggle');
toggle.addEventListener('change', () => {
  document.body.classList.toggle('dark-mode', toggle.checked);
});

const authBox = document.getElementById('authBox');
const panelContent = document.getElementById('panelContent');
const loginForm = document.querySelector('.form.login');
const registerForm = document.querySelector('.form.register');

function toggleForm() {
  authBox.classList.toggle('active');
  const isActive = authBox.classList.contains('active');

  panelContent.innerHTML = isActive
    ? `<h2>Welcome Back</h2><p>Already have an account?</p><button onclick="toggleForm()">Login</button>`
    : `<h2>New here?</h2><p>Join NetWork and connect professionally.</p><button onclick="toggleForm()">Sign Up</button>`;

  // Shift forms to the right half of auth-box
  loginForm.style.left = isActive ? '0%' : '50%';
  registerForm.style.left = isActive ? '50%' : '0%';
}

// Initialize default view
loginForm.style.left = '50%';
registerForm.style.left = '0%'; 