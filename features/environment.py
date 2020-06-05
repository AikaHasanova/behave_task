from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox(executable_path=r'C:\Users\hasan\OneDrive\Desktop\geckodriver-v0.26.0-win64\geckodriver')
    return context
def after_all(context):
    context.browser.close()