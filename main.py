from utils.extract import scrape_website
from utils.transform import transform_data
from utils.load import save_csv, save_google_sheets, save_database

def main():
    base_url = "https://fashion-studio.dicoding.dev/"
    all_products = []
    
    # Scrape the main page
    print("Scraping main page...")
    try:
        products = scrape_website(base_url)
        all_products.extend(products)
    except Exception as e:
        print(f"Error scraping main page: {e}")
        
    # Scrape the subpages
    print("Scraping subpages...")
    try:
        for i in range(2, 51):
            subpage_url = f"{base_url}page{i}"
            products = scrape_website(subpage_url)
            all_products.extend(products)
    except Exception as e:
        print(f"Error scraping subpages: {e}")
    
    transformed_data = transform_data(all_products)
    save_csv(transformed_data, 'products.csv')
    save_google_sheets(transformed_data, '1qWLxnnAtyXLKWg4NnChmSc_f3wt1JCrOwrEiKA9Xpas', 'Sheet1!A1', '../google-sheets-api..json')
    save_database(transformed_data)
    print("Data processing completed successfully.")
    
if __name__ == "__main__":
    main()