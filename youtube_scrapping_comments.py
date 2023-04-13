#importing the required modules to do our tasks
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time

#selenium gives us the freedom to automate our task on web browser

def scrapcomment(url):
    option=webdriver.ChromeOptions()
    option.add_argument("--headless")   #taaki wo us link ko khole na isse humara time bhee bachega
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=option)
    driver.get(url)
    time.sleep(5)
    prev_h=0
    while True:
          #Below script is run so that we can calculate the total height of our page ,height is calculated to reach till the last of the page 
          height=driver.execute_script("""
    function getActualHeight(){
        return Math.max(
            Math.max(document.body.scrollHeight,document.documentElement.scrollHeight),
            Math.max(document.body.offsetHeight,document.documentElement.offsetHeight),
            Math.max(document.body.clientHeight,document.documentElement.clientHeight)
        );
    }
    return getActualHeight()""")
          driver.execute_script(f"window.scrollTo({prev_h},{prev_h+400})")
          time.sleep(3)     #here we add sleep because comments also take some time to load only scrolling will not work out
          prev_h+=400       #we are incrementing the height by 400 one can use different number or can directly scroll till the height
          if prev_h>=height:    #if our previous height is more than the total calculated height than we can stop this loop
               break
          
        

  

    bsoup=bs(driver.page_source,'html.parser')
    driver.quit()
    title_text_div=bsoup.select_one('#container h1')        #for single video
    title=title_text_div and title_text_div.text      #to get title
    comment_div=bsoup.select("#content #content-text")
    comment_list=[x.text for x in comment_div]
    print(title,comment_div)
    


if __name__=="__main__":
    urls="https://www.youtube.com/watch?v=oA8brF3w5XQ"
    scrapcomment(urls)