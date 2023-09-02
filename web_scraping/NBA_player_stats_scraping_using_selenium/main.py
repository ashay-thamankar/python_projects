import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, StaleElementReferenceException, \
    ElementNotInteractableException
from selenium.webdriver.common.by import By

nba_url = 'https://www.nba.com/stats/players/traditional?PerMode=Totals&dir=-1&sort=PTS'
driver = webdriver.Chrome()

driver.get(nba_url)
time.sleep(1)

# to clear the cookies
try:
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
except:
    pass
time.sleep(2)

names = []
teams = []
ages = []
games_played = []
wins = []
loose = []
min_played = []
points = []
field_goal_made = []
field_goal_attempt = []
three_made = []
three_attempted = []
free_made = []
free_attempted = []
of_r = []
df_r = []
reb = []
assist = []
turnover = []
steals = []
blocks = []

# to get the total number of pages
last_element = int(driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div['
                                       '1]/div[4]').text.split(
    ' ')[1])
for _ in range(last_element):
    time.sleep(.1)
    all_table_head = driver.find_elements(By.CSS_SELECTOR, '.Crom_body__UYOcU tr')
    for head in all_table_head:
        time.sleep(0.1)
        all_player_head = head.find_elements(By.CSS_SELECTOR, 'td')

        try:
            names.append(all_player_head[1].text)
            teams.append(all_player_head[2].text)
            ages.append(all_player_head[3].text)
            games_played.append(all_player_head[4].text)
            wins.append(all_player_head[5].text)
            loose.append(all_player_head[6].text)
            min_played.append(all_player_head[7].text)
            points.append(all_player_head[8].text)
            field_goal_made.append(all_player_head[9].text)
            field_goal_attempt.append(all_player_head[10].text)
            three_made.append(all_player_head[12].text)
            three_attempted.append(all_player_head[13].text)
            free_made.append(all_player_head[15].text)
            free_attempted.append(all_player_head[16].text)
            of_r.append(all_player_head[18].text)
            df_r.append(all_player_head[19].text)
            reb.append(all_player_head[20].text)
            assist.append(all_player_head[21].text)
            turnover.append(all_player_head[22].text)
            steals.append(all_player_head[23].text)
            blocks.append(all_player_head[24].text)

        except StaleElementReferenceException as err:
            print(err)

    time.sleep(0.1)
    next_button = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]')
    time.sleep(.3)
    next_button.click()

time.sleep(1)

# put the form url link
forms_url = 'https://docs.google.com/forms/d/e/1FAIpQLSctsxk8l1dTVFfVRFKQkz2iLmYZ-qq8WHlrl9zRPr18TzTbfQ/viewform?usp=sf_link'
driver_f = webdriver.Chrome()

driver_f.get(forms_url)

all_elements = [names, teams, ages, games_played, wins, loose, min_played, points, field_goal_made, field_goal_attempt,
                three_made, three_attempted, free_made, free_attempted, of_r, df_r, reb, assist, turnover, steals,
                blocks]

for m in range(len(names)):
    all_div = driver_f.find_elements(By.CSS_SELECTOR, '.o3Dpx .Qr7Oae')
    for n in range(len(all_div)):
        time.sleep(1)
        indi = all_div[n].find_element(By.CSS_SELECTOR, '.Xb9hP input')
        try:
            time.sleep(0.5)
            indi.send_keys(all_elements[n][m])
        except ElementNotInteractableException as err:
            print(err)
    driver_f.find_element(By.CSS_SELECTOR, '.lRwqcd div').click()
    time.sleep(1)
    driver_f.find_element(By.LINK_TEXT, 'Submit another response').click()
    time.sleep(1)

time.sleep(5)
driver.quit()
driver_f.quit()
