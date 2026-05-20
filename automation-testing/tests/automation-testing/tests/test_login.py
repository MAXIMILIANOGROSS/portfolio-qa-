import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com")
    
    def test_valid_login(self):
        """Test login con credenciales válidas"""
        # Step 1: Click en login
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()
        
        # Step 2: Enter username
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testuser@gmail.com")
        
        # Step 3: Enter password
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("Test123!")
        
        # Step 4: Click submit
        submit = self.driver.find_element(By.ID, "submit")
        submit.click()
        
        # Expected: Usuario logueado
        assert "dashboard" in self.driver.current_url
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
