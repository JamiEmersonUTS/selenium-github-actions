from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver



# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute file path by joining the script's directory with the relative file path
file_path = os.path.join(script_dir, 'files', 'CV_Jane_Smith.docx')



s = Service('/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")


driver = webdriver.Chrome(service=s, options=options)
# navigate to eoi webpage
driver.get('https://cad-business-sandpit.itu.uts.edu.au/cad/eoi')

try:


    # Click Next button
    next_button = driver.find_element(By.ID, "but_nextnext").click()


    # Fill form  Page one
    select_title = Select(driver.find_element(By.ID, 'title'))
    select_title.select_by_visible_text('Miss')

    first_name = driver.find_element(By.ID, "first_name")
    first_name.send_keys("Jane")

    family_name = driver.find_element(By.ID, "family_name")
    family_name.send_keys("Smith")

    residential_address = driver.find_element(By.ID, "residential_addr")
    residential_address.send_keys("54489, Park Avenue, New York, NYC 80093")

    email_address = driver.find_element(By.ID, "email")
    email_address.send_keys("hello@email.com")

    mobile_phone = driver.find_element(By.ID, "mobile")
    mobile_phone.send_keys("0432 995 996")

    home_phone = driver.find_element(By.ID, "phone_home")
    home_phone.send_keys("0432 995 543")

    work_phone = driver.find_element(By.ID, "phone_work")
    work_phone.send_keys("0432 995 759")

    uts_staff_id = driver.find_element(By.ID, "uts_staff_id")
    uts_staff_id.send_keys("743965")


    aus_citizen = driver.find_element(
        By.XPATH, "//input[@name='right_to_work' and @value='Australian Citizen']").click()


    next_button2 = driver.find_element(
        By.XPATH, '//*[@id="frm_pd"]/div/div/div[9]/div[2]/button').click()

    #Sotware Skills
    excel = Select(driver.find_element(By.ID, 'sp_excel'))
    excel.select_by_visible_text('Some proficiency')

    SPSS_STATA = Select(driver.find_element(By.ID, 'sp_spss'))
    SPSS_STATA.select_by_visible_text('Some proficiency')

    tableau = Select(driver.find_element(By.ID, 'sp_tableau'))
    tableau.select_by_visible_text('Some proficiency')

    python = Select(driver.find_element(By.ID, 'sp_python'))
    python.select_by_visible_text('Some proficiency')

    R = Select(driver.find_element(By.ID, 'sp_r'))
    R.select_by_visible_text('Some proficiency')

    powerBI = Select(driver.find_element(By.ID, 'sp_pbi'))
    powerBI.select_by_visible_text('Some proficiency')

    microsoft_dynamics = Select(driver.find_element(By.ID, 'sp_mdym'))
    microsoft_dynamics.select_by_visible_text('Some proficiency')

    uts_relationship = Select(driver.find_element(By.ID, 'uts_rel'))
    uts_relationship.select_by_visible_text('Current student PhD of UTS')

    previous_work = driver.find_element(By.CSS_SELECTOR, "input[type= 'radio']").click()

    education = Select(driver.find_element(By.ID, 'edu_type'))
    education.select_by_visible_text('Secondary')

    degree_level = Select(driver.find_element(By.ID, 'highest_qual'))
    degree_level.select_by_visible_text('Masters Degree')


    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type= 'checkbox']")
    chk = [checkbox for checkbox in checkboxes]
    for i in chk:
        if not i.is_selected():
            i.click()

    text_boxes = driver.find_elements(By.CLASS_NAME, "form-control")
    txt = [forms for forms in text_boxes]
    for i in txt:
        if not i.send_keys():
            i.send_keys("hello world")

    next_button3 = driver.find_element(
        By.XPATH, '//*[@id="frm_se"]/div[24]/div[2]/button').click()

    choose_file = driver.find_element(By.ID, "file_up").send_keys(file_path)

    supporting_type = Select(driver.find_element(By.ID, 'doc_type'))
    supporting_type.select_by_visible_text('A Resume or CV')

    brief_description = driver.find_element(By.ID, 'doc_title').send_keys("This is my CV")

    driver.implicitly_wait(5)

    upload_doc_button = driver.find_element(
        By.XPATH, '//*[@id="frm_att"]/div[1]/div[2]/div[3]/div[2]/div[2]/div/button').click()

    choose_file = driver.find_element(By.ID, "file_up").send_keys(file_path)

    supporting_type = Select(driver.find_element(By.ID, 'doc_type'))
    supporting_type.select_by_visible_text('Evidence of Highest Qualification')

    brief_description = driver.find_element(By.ID, 'doc_title').send_keys("This is my testaumar")

    upload_doc_button = driver.find_element(
        By.XPATH, '//*[@id="frm_att"]/div[1]/div[2]/div[3]/div[2]/div[2]/div/button').click()

    next_button4 = driver.find_element(
        By.XPATH, '//*[@id="frm_att"]/div[2]/div[2]/button').click()

    dont_disclose = driver.find_element(
    By.XPATH, '//*[@id="subm_form"]/div[1]/div/div[2]/div/input[2]').click()

    accessibility = driver.find_element(By.ID, 'acs_req').send_keys("Hello World")
    personal_email = driver.find_element(By.ID, 'cf_email_addr').send_keys("hello@email.com")

    acknowledge = driver.find_element(By.ID, "cbk_ack").click()

    #submit_application = driver.find_element(By.ID, "myseoi").click()
    

    if driver.current_url.startswith('https://'):
        print("The website has a valid certificate.")
    else:
        print("The website does not have a valid certificate.")

    url = driver.current_url
    print(url)

finally:
    driver.quit()
