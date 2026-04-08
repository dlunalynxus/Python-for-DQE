# Import datetime module to work with dates
from datetime import datetime

# File where all records will be stored
FILE_NAME = "news_feed.txt"


# Function to write content to file
def publish_to_file(content):
    # Open file in append mode ("a") to add new records at the end
    with open(FILE_NAME, "a") as file:
        # Write content and add line break
        file.write(content + "\n\n")


# Function to create News record
def create_news():
    # Ask user for news text
    text = input("Enter news text: ")
    
    # Ask user for city
    city = input("Enter city: ")
    
    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Format record
    news = f"News -------------------------\n{text}\n{city}, {current_date}"
    
    # Publish to file
    publish_to_file(news)


# Function to create Private Ad
def create_private_ad():
    # Ask user for ad text
    text = input("Enter ad text: ")
    
    # Ask user for expiration date
    expiration_input = input("Enter expiration date (YYYY-MM-DD): ")
    
    # Convert string to date
    expiration_date = datetime.strptime(expiration_input, "%Y-%m-%d")
    
    # Get current date
    current_date = datetime.now()
    
    # Calculate days left
    days_left = (expiration_date - current_date).days
    
    # Format record
    ad = f"Private Ad -------------------\n{text}\nActual until: {expiration_input}, {days_left} days left"
    
    # Publish to file
    publish_to_file(ad)


# Function for custom record (unique one)
def create_quote():
    # Ask user for quote text
    text = input("Enter quote: ")
    
    # Ask for author
    author = input("Enter author: ")
    
    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Custom rule: always uppercase quote + include author
    quote = f"Quote ------------------------\n{text.upper()}\nAuthor: {author} | Date: {current_date}"
    
    # Publish to file
    publish_to_file(quote)


# Main menu function
def main():
    while True:
        # Show menu options
        print("\nSelect what you want to add:")
        print("1 - News")
        print("2 - Private Ad")
        print("3 - Quote (custom)")
        print("0 - Exit")
        
        # Get user choice
        choice = input("Your choice: ")
        
        # Process user choice
        if choice == "1":
            create_news()
        elif choice == "2":
            create_private_ad()
        elif choice == "3":
            create_quote()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")


# Entry point
if __name__ == "__main__":
    main()