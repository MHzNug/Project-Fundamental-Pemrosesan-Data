import unittest
from unittest.mock import patch, MagicMock
from utils.extract import scrape_website

class TestScrapeWebsite(unittest.TestCase):
    
    @patch('utils.extract.requests.get')
    def test_scrape_website_success(self, mock_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <body>
                <div class="collection-card">
                    <h3 class="product-title">Test Product</h3>
                    <div class="price-container">$10</div>
                    <p>Rating: ⭐ 3 / 5</p>
                    <p>Colors: 2 Color</p>
                    <p>Size: M</p>
                    <p>Gender: Men</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        url = "https://fashion-studio.dicoding.dev/"
        
        # Call the function to test
        result = scrape_website(url)
        
        # Assert the result
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn('title', result[0])
        self.assertEqual(result[0]['title'], 'Test Product')
        
    @patch('utils.extract.requests.get')
    def test_scrape_website_failure(self, mock_get):
        # Mock a failed response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        url = "https://fashion-studio.dicoding.dev/"
        
        # Call the function to test and assert it raises an exception
        with self.assertRaises(Exception) as context:
            scrape_website(url)
            self.assertIn('Error fetching data from', str(context.exception))