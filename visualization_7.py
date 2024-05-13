import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
def visualize_price_trend(data):
    # Convert the date strings to datetime objects
    dates = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in data['Date']]

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the price data
    ax.plot(dates, data['Price(₹)'])

    # Set the title and axis labels
    ax.set_title('iPhone 15 Price Trend')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (₹)')

    # Rotate the x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Set the x-axis tick format to display dates nicely
    date_formatter = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_formatter)

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Display the plot
    plt.show()