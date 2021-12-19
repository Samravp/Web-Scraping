# Web Scraping

This project was done in 2 steps;

## **Step 1 - Scraping**

Initial scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

A Jupyter Notebook file called mission_to_mars.ipynb was created and used to complete all of the scraping and analysis tasks. 

The following outlines what was scraped from web.

- **NASA Mars News**

 Mars News Site was scraped and the latest News Title and Paragraph Text were collected. 
 
 The article and other news information were assigned to variables that you could be referenced later.
 
 - **JPL Mars Space Images - Featured Image**

Utilising splinter, I navigated to the Mars Space Images website and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.

- **Mars Facts**

In this section, I used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc from Mars Facts webpage.

Then I used Pandas to convert the data to a HTML table string.

- **Mars Hemispheres**

After visiting the astrogeology site, a high resolution images for each of Mar's hemispheres were obtained using web scraping.

I saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 

A Python dictionary was used to store the data using the keys img_url and title.

The dictionary was appended with the image url string and the hemisphere title to a list. 

This list contained one dictionary for each hemisphere.

## **Step 2 - MongoDB and Flask Application**

I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

I started by converting my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

Next, a route called /scrape was created that imports scrape_mars.py script and calls the scrape function.

A root route / was creted also, this will query the Mongo database and pass the mars data into an HTML template to display the data.

Finally, a template HTML file called index.html was created that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
