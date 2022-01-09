# Housing-Data-Automation

In this project I used BeautifulSoup and Selenium Webdriver to collect data from over 220 house listings in the Greater Toronto Area from Zillow. I then used 
Selenium Webdriver to auto input all of this data onto a google sheets. My goal was to create a forecasting tool that would allow me to forecast average monthly
listing prices in the short term. I used the requests module in Python, along with BeautifulSoup to webscrape relevant listing data. I then organized this data into Python datastructures
and datatypes such as lists and tuples. I then used Selenium Webdriver to automate my browser to loop through each tuple, inputting over 225 houses worth of data into a spreadsheet!

Upon creating the database using Python and Selenium Webdriver, I decided to create a graph. Since the data I collected was for 225 house listings in January 2022, I found the mean of these 225 listings. I then did some research,
and found data from https://toronto.listing.ca/real-estate-price-history.htm and Stats Canada that I could use to build my forecasting tool by incorporating previous months.

After doing all of that, I then plotted all of this data using appropriate graphing technology. I performed nonlinear regression on this graph, and then I used
the equation obtained from this regression to forecast average listing prices in the short term (next 1-2 months). 

This tool is incredibly useful as it allows me to collect and analyze data using real-time house listings, instead of waiting for the realtors to release their outdated monthly
dataset. This tool can then be used to forecast and analyze housing prices using the latest house listings, and can be extremely useful for first-time house buyers or
even realtors. While I used this tool to collect house listing prices in the GTA for January 2022, it can be deployed to collect various other segments of data to create an even more detailed database.

# Graph

![img](https://github.com/sdesai13/Housing-Data-Automation/blob/main/housingautomationss.png)

# How to execute the program

In order to execute this script onto your local development environment, you will need to get your HTTP headers information (link in the .py file) and create your own spreadsheet to input data into.
You may also want to customize what data you're scraping for, and how you are processing it. Simply run the script and let it automate the data process for you!
Feel free to contact me with any questions about the code or how to use it correctly in your local environment.

