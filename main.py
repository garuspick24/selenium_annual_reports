from selenium import webdriver

topic_search = input("Enter the topic you want to search: ")
topic_search = topic_search.replace(" ", "+")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)

for i in range(1):
    elements = browser.get('https://www.google.com/search?q=' + topic_search + '&start=' + str(i))

list = [

]
