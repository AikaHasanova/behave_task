from behave import when, then


@when('click the link "{link}" ')
def step_click_the_link(context, link):
    context.browser.get(link)
@then('the should be title"{title}" ')
def step_test_title(context, title):
    assert context.browser.title == title
@then('check the email input')
def step_test_email(context):
    assert context.browser.find_element_by_css_selector('#email')
@then('check the password input')
def step_test_password(context):
    assert context.browser.find_element_by_css_selector('#pass')
