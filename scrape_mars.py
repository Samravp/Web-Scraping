from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path':ChromeDriverManager().install()}
    Browser("chrome", **executable_path, headless=False)

    # NASA Mars News
    # URL of the page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find the division part of latest news 
    Dates = soup.find_all('div', class_='list_date')
    titles = soup.find_all('div', class_='content_title')
    paragraphs = soup.find_all('div', class_='article_teaser_body')

    # Identify and return the latest date, title and paragraph
    latest_date=Dates[0].text
    latest_title = titles[1].text
    latest_article = paragraphs[0].text

    # JPL Mars Space Images
    # URL of the next page to be scraped
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Create the BeautifulSoup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find the Image url
    featured_image = soup.find("img", class_ = "headerimage fade-in")

    # Display the complete url string for the featured image
    featured_image_url = url + featured_image["src"]
    print(featured_image_url)

    # # Mars facts
    # URL of page to be scraped
    url = 'https://galaxyfacts-mars.com/'

    # Retrieve the page
    browser.visit(url)

    # Getting all tables from the page as a list
    tables = pd.read_html(url)

    # Store the table from website in pandas DataFrame
    mars_facts_df = pd.DataFrame(tables[1])

    mars_facts_df

    mars_facts_df.columns = ['Description','Mars Values']
    mars_facts_df.set_index('Description', inplace=True)
    mars_facts_df

    # Convert DataFrame to HTML string
    mars_facts = mars_facts_df.to_html(header = True, index = True)
    print(mars_facts)

    # Mars Hemispheres
    # URL of page to be scraped
    url = 'https://marshemispheres.com/'

    # Open the browser
    browser.visit(url)

    # Create BeautifulSoup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # Hemisphere in the HTML are saved in description class
    Hms = soup.find_all("div", class_ = "description")

    # Initialise the emplty lists
    urls = []
    titles = []

    # Loop through hemispheres and save urls and titles in a list
    for Hm in Hms:
        urls.append(url + Hm.find('a')['href'])
        titles.append(Hm.find('h3').text.strip())
    
    print(titles)

    # Initialise an emplty list for image urls
    img_urls = []

    for url in urls:
        browser.visit(url)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    
    url = url+soup.find('img',class_='wide-image')['src']
    img_urls.append(url)
    
    img_urls
    hemisphere_image_urls = []

    for i in range(len(titles)):
        hemisphere_image_urls.append({'title':titles[i],'img_url':img_urls[i]})
        hemisphere_image_urls

    browser.quit()

    # Assign scraped data to a page
    Mars_data= {
    "news_date":latest_date,
    "news_title":latest_title,
    "news_p":latest_article,
    "features_img":featured_image_url,
    "mars_table":mars_facts,
    "hemispheres":hemisphere_image_urls
    }
    return Mars_data