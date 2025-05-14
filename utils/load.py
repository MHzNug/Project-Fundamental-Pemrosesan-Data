import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def save_csv(df, filename = 'products.csv'):
    """
    Save the DataFrame to a CSV file.
    """
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    
def save_google_sheets(df, spreadsheet_id, range_name, credentials_file):
    """
    Save the DataFrame to a Google Sheet.
    """
    # Load credentials from the service account file
    creds = Credentials.from_service_account_file(credentials_file)
    
    # Build the Google Sheets API service
    service = build('sheets', 'v4', credentials=creds)
    
    # Convert DataFrame to a list of lists
    values = [df.columns.values.tolist()] + df.values.tolist()
    
    # Prepare the request body
    body = {
        'values': values
    }
    
    # Call the Sheets API to update the specified range
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
    
    print(f"Data saved to Google Sheet: {spreadsheet_id} in range: {range_name}")
    
def save_database(df, db_connection=None, table_name='products'):
    """
    Save the DataFrame to a database.
    """
    try:
        username = "your_username"
        password = "your_password"
        host = "your_host"
        port = "your_port"
        database = "your_database"
        
        # Create a database connection
        db_connection = f"postgresql://{username}:{password}@{host}:{port}/{database}"
        # Assuming you are using SQLAlchemy
        engine = create_engine(db_connection)
        
    except ImportError:
        raise ImportError("SQLAlchemy is not installed. Please install it to use this function.")
    except Exception as e:
        raise Exception(f"Error creating database connection: {e}")
    
    if db_connection is None:
        raise ValueError("Database connection is not provided.")
    
    # Assuming db_connection is a SQLAlchemy engine
    df.to_sql(table_name, con=db_connection, if_exists='replace', index=False)
    print(f"Data saved to database table: {table_name}")