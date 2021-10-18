import behave
from selenium.webdriver import Chrome

@given(u'User is on registration page')
def step_impl(context):

    path = "/usr/local/bin/chromedriver"
    context.driver = Chrome(executable_path=path)

    # open the page 
    context.driver.get("https://thetestingworld.com/testings/")


    @when(u'User enters username')
    def step_impl(context):
        context.driver.find_element_by_name('fld_username').send_keys('abcd')


    @when(u'User enters email id')
    def step_impl(context):
        context.driver.find_element_by_name('fld_email').send_keys('abc@gmail.com')


    @when(u'User enters password')
    def step_impl(context):
        context.driver.find_element_by_name('fld_password').send_keys('abc123')


    @when(u'User clicks on signup button')
    def step_impl(context):
        context.driver.find_element_by_xpath('//input[@type="submit" and @value="Sign up"]').click()


    @then(u'User is registered successfully')
    def step_impl(context):
        print('Registered')


    @when(u'User enters duplicate username')
    def step_impl(context):
        print('Not Registered')