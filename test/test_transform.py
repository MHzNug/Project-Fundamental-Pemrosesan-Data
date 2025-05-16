import unittest
import pandas as pd
from utils.transform import transform_data

class TestTransformData(unittest.TestCase):
    
    def test_transform_data(self):
        # Sample input data
        products = [{
                'title': 'Test Product',
                'price': '$19.99',
                'rating': '3.9',
                'color': '3 Colors',
                'size': 'M',
                'gender': 'Men'
                }]
        
        # Call the function to test
        transformed_data = transform_data(products)
        
        # Assert the result
        self.assertEqual(len(transformed_data), 1)
        self.assertIn('title', transformed_data.columns)
        self.assertIn('price', transformed_data.columns)
        self.assertIn('rating', transformed_data.columns)
        self.assertIn('color', transformed_data.columns)
        self.assertIn('size', transformed_data.columns)
        self.assertIn('timestamp', transformed_data.columns)
        self.assertTrue(isinstance(transformed_data['price'][0], float))
        self.assertTrue(isinstance(transformed_data['rating'][0], float))
        self.assertEqual(transformed_data['title'][0], 'Test Product')
        
    def test_invalid(self):
        # Sample input data with invalid values
        products = [{
                'title': 'Test Product',
                'price': '$19.99',
                'rating': '3.9',
                'color': '3 Colors',
                'size': 'M',
                'gender': 'Men'
                },
                {
                'title': 'Unknown Product',
                'price': '$0.00',
                'rating': '',
                'color': '',
                'size': '',
                'gender': ''
                }]
        
        # Call the function to test
        transformed_data = transform_data(products)
        
        # Assert the result
        self.assertEqual(len(transformed_data), 1)
        self.assertIn('title', transformed_data.columns)
        self.assertIn('price', transformed_data.columns)
        self.assertIn('rating', transformed_data.columns)
        self.assertIn('color', transformed_data.columns)
        self.assertIn('size', transformed_data.columns)
        self.assertIn('timestamp', transformed_data.columns)
    
    if __name__ == '__main__':
        unittest.main()
        
        