<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simlane.ai - Secure Access</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #064e3b 0%, #10b981 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .login-container {
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            width: 100%;
            max-width: 440px;
            padding: 48px;
        }
        
        .logo-section {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .logo {
            font-size: 32px;
            font-weight: 700;
            color: #10b981;
            letter-spacing: -0.02em;
            margin-bottom: 8px;
        }
        
        .tagline {
            color: #6b7280;
            font-size: 14px;
            font-weight: 500;
            letter-spacing: 0.02em;
        }
        
        h2 {
            color: #111827;
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 8px;
            letter-spacing: -0.01em;
        }
        
        .subtitle {
            color: #6b7280;
            font-size: 14px;
            margin-bottom: 32px;
            line-height: 1.5;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            color: #374151;
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 8px;
        }
        
        input {
            width: 100%;
            padding: 12px 16px;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            font-size: 14px;
            transition: all 0.2s;
            font-family: inherit;
        }
        
        input:focus {
            outline: none;
            border-color: #10b981;
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
        }
        
        input::placeholder {
            color: #9ca3af;
        }
        
        .password-container {
            position: relative;
        }
        
        .btn-primary {
            width: 100%;
            padding: 12px 24px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            margin-top: 8px;
        }
        
        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 8px 16px rgba(16, 185, 129, 0.3);
        }
        
        .btn-primary:active {
            transform: translateY(0);
        }
        
        .divider {
            text-align: center;
            color: #9ca3af;
            font-size: 13px;
            margin: 24px 0;
            position: relative;
        }
        
        .divider::before,
        .divider::after {
            content: '';
            position: absolute;
            top: 50%;
            width: calc(50% - 30px);
            height: 1px;
            background: #e5e7eb;
        }
        
        .divider::before {
            left: 0;
        }
        
        .divider::after {
            right: 0;
        }
        
        .security-badge {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            margin-top: 32px;
            padding-top: 24px;
            border-top: 1px solid #e5e7eb;
            color: #6b7280;
            font-size: 13px;
        }
        
        .lock-icon {
            width: 16px;
            height: 16px;
            fill: #10b981;
        }
        
        .client-info {
            background: #f9fafb;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 24px;
            border-left: 3px solid #10b981;
        }
        
        .client-info h3 {
            color: #111827;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 4px;
        }
        
        .client-info p {
            color: #6b7280;
            font-size: 13px;
        }
        
        .remember-me {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
            margin-top: -8px;
        }
        
        .checkbox-wrapper {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .checkbox-wrapper input[type="checkbox"] {
            width: 16px;
            height: 16px;
            accent-color: #10b981;
            cursor: pointer;
        }
        
        .checkbox-wrapper label {
            margin: 0;
            font-size: 14px;
            color: #374151;
            cursor: pointer;
        }
        
        .forgot-link {
            color: #10b981;
            font-size: 14px;
            text-decoration: none;
            font-weight: 500;
        }
        
        .forgot-link:hover {
            text-decoration: underline;
        }
        
        @media (max-width: 480px) {
            .login-container {
                padding: 32px 24px;
            }
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo-section">
            <div class="logo">Simlane.ai</div>
            <div class="tagline">INTELLIGENT ANALYTICS PLATFORM</div>
        </div>
        
        <h2>Sign in to your account</h2>
        <p class="subtitle">Enter your credentials to access the analytics dashboard</p>
        
        <form onsubmit="handleLogin(event)">
            <div class="form-group">
                <label for="email">Email address</label>
                <input 
                    type="email" 
                    id="email" 
                    name="email" 
                    placeholder="you@company.com" 
                    required
                    autocomplete="email"
                >
            </div>
            
            <div class="form-group">
                <label for="password">Password</label>
                <div class="password-container">
                    <input 
                        type="password" 
                        id="password" 
                        name="password" 
                        placeholder="Enter your password" 
                        required
                        autocomplete="current-password"
                    >
                </div>
            </div>
            
            <div class="remember-me">
                <div class="checkbox-wrapper">
                    <input type="checkbox" id="remember" name="remember">
                    <label for="remember">Remember me</label>
                </div>
                <a href="#" class="forgot-link">Forgot password?</a>
            </div>
            
            <button type="submit" class="btn-primary">
                Sign in
            </button>
        </form>
        
        <div class="security-badge">
            <svg class="lock-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
            </svg>
            <span>Secured with 256-bit SSL encryption</span>
        </div>
    </div>
    
    <script>
        function handleLogin(event) {
            event.preventDefault();
            
            // Get form values
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Demo credentials
            const VALID_EMAIL = 'demo@simlane.ai';
            const VALID_PASSWORD = 'SimlaneVet2024';
            
            // Validate credentials
            if (email === VALID_EMAIL && password === VALID_PASSWORD) {
                // Show loading state
                const button = event.target.querySelector('.btn-primary');
                const originalText = button.textContent;
                button.textContent = 'Signing in...';
                button.disabled = true;
                
                // Simulate authentication delay
                setTimeout(() => {
                    // Store session
                    sessionStorage.setItem('simlane_authenticated', 'true');
                    sessionStorage.setItem('simlane_user', email);
                    
                    // Success message
                    alert('Authentication successful! Redirecting to dashboard...');
                    button.textContent = 'Success!';
                    button.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
                    
                    // In production/Streamlit, redirect to dashboard here
                    // window.location.href = '/dashboard';
                    
                }, 1500);
            } else {
                // Show error
                const button = event.target.querySelector('.btn-primary');
                const originalText = button.textContent;
                button.textContent = 'Invalid credentials';
                button.style.background = 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)';
                
                // Reset after delay
                setTimeout(() => {
                    button.textContent = originalText;
                    button.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
                }, 2000);
            }
        }
        
        // Check if already authenticated
        window.addEventListener('load', () => {
            if (sessionStorage.getItem('simlane_authenticated') === 'true') {
                // Could auto-redirect to dashboard
                console.log('User already authenticated');
            }
        });
    </script>
</body>
</html>
