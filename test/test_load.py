import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import save_csv, save_google_sheets

class TestLoadFunctions(unittest.TestCase):
    
    @patch('utils.load.pd.DataFrame.to_csv')
    def test_save_csv(self, mock_to_csv):
        # Create a sample DataFrame
        df = pd.DataFrame({
            'title': ['Test Product'],
            'price': [19.99],
            'rating': [3.9],
            'color': ['Red'],
            'size': ['M'],
            'gender': ['Men'],
            'timestamp': [pd.Timestamp.now()]
        })
        
        # Call the function to test
        save_csv(df, 'test.csv')
        
        # Assert the result
        mock_to_csv.assert_called_once_with('test.csv', index=False)
        
    @patch('utils.load.build')
    @patch('utils.load.Credentials.from_service_account_file')
    def test_save_google_sheets(self, mock_creds, mock_build):
        # Create a sample DataFrame
        df = pd.DataFrame({
            'title': ['Test Product'],
            'price': [19.99],
            'rating': [3.9],
            'color': ['Red'],
            'size': ['M']
        })
        
        # Mock the Google Sheets API
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        
        # Call the function to test
        save_google_sheets(df, 'spreadsheet_id', 'Sheet1!A1', 'credentials.json')
        
        # Assert the result
        mock_creds.assert_called_once_with('credentials.json')
        mock_build.assert_called_once_with('sheets', 'v4', credentials=mock_creds())
        mock_service.spreadsheets().values().update.assert_called_once()
        
    if __name__ == '__main__':
        unittest.main()