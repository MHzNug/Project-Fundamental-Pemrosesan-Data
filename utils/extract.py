import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        raise Exception(f"Error fetching data from {url}: {e}")
    
    try:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        
        # Find all product elements
        product_elements = soup.find_all('div', class_='collection-card')
        
        # Loop through each product element and extract details
        for product in product_elements:
            title_element = product.find('h3', class_='product-title')
            title = title_element.text.strip() if title_element else None

            price_element = product.find('div', class_='price-container')
            price = price_element.text.strip() if price_element else None

            rating_element = product.find('p', string=lambda text: text and 'Rating' in text)
            rating = rating_element.text.strip() if rating_element else None

            color_element = product.find('p', string=lambda text: text and 'Colors' in text)
            color = color_element.text.strip() if color_element else None

            size_element = product.find('p', string=lambda text: text and 'Size' in text)
            size = size_element.text.strip() if size_element else None

            gender_element = product.find('p', string=lambda text: text and 'Gender' in text)
            gender = gender_element.text.strip() if gender_element else None
            
            # Append the product details to the list
            products.append({
                'title': title,
                'price': price,
                'rating': rating,
                'color': color,
                'size': size,
                'gender': gender
            })
        
        return products
    
    except Exception as e:
        raise Exception(f"Error parsing HTML: {e}")