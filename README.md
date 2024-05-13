# Web-Scraping_project

PROJECT TITLE: iPhone 15 Price Tracker
PROJECT DESCRIPTION:
This project is a web scraping application that periodically scrapes the product page of Flipkart for the iPhone 15, one of India's biggest e-commerce platforms, and extracts the current price of the iPhone 15, along with the rating and several other details, and stores the relevant aspects in a CSV file. Moreover, this application provides mail services when the price of the product goes below a certain value.
FEATURES:
1.	Web scraping was performed using Python's requests and BeautifulSoup APIs.
2.	Data extraction and preprocessing for the product name, price, and rating.
3.	The latest findings were saved in a CSV file with a timestamp.
4.	An automatic email was sent when the price fell below a predefined threshold.
5.	The price development has been visualized over time with the aid of matplotlib.
Requirements
•	Python 3.x
•	Required Python libraries: 
o	requests
o	beautifulsoup4
o	csv
o	datetime
o	smtplib
o	pandas
o	matplotlib
File Structure	
•	DateTime_3.py: Retrieves the current date.
•	Excel_2.py: Handles CSV file operations (writing and appending data).
•	WebScrap_1.py: Performs web scraping on the Flipkart product page and extracts relevant data.
•	mail_6.py: Contains the function to send email notifications.
•	visualization_7.py: Implements data visualization for price trends using matplotlib.
•	ProductTracker_5.py: The main script that ties all components together and runs the price tracking process.
Usage
1.	Clone the repository or download the project files.
2.	Install the required Python libraries using pip install -r requirements.txt.
3.	Configure the email settings in mail_6.py with your email credentials.
4.	Optionally, you can modify the price threshold and other settings as per your needs.
5.	Run the ProductTracker_5.py script to start the price tracking process.
6.	The script will periodically scrape the Flipkart product page, update the CSV file with the latest data, and send an email notification if the price drops below the set threshold.
7. The price trend visualization will be displayed each time the script is run.
Contributing
Contributions welcome! Please file issues or submit pull requests if you find any bugs or have suggestions for improvement.

