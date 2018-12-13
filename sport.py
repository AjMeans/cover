from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import config

from constants import OVER_UNDER, AGAINST_THE_SPREAD, MONEY_LINE, GAME_STATUS_FINAL


class Sport(object):

    def __init__(self, sport, percentage):
        self.sport = sport
        self.percentage = percentage

    def get_data(self, driver):
        game_data = get_games(driver)

        try:
            for game, value in game_data.iteritems():
                # Navigate to the game page and sleep for 3 seconds to make sure the page has time to load
                driver.get(game)

                element_present = EC.presence_of_element_located((By.CLASS_NAME, 'teams'))
                WebDriverWait(driver, config.TIMEOUT).until(element_present)

                status = value['game_status']
                teams = driver.find_element_by_class_name('teams')
                hometeam = teams.find_element_by_class_name('home').text. \
                    replace('@', '').replace(' VS.', '').strip()
                awayteam = teams.find_element_by_class_name('away').text. \
                    replace('@', '').replace(' VS.', '').strip()
                picks = driver.find_element_by_class_name('picks')
                section = picks.find_elements_by_class_name('pick-wrapper')

                for data in section:
                    # proj_score = data.find_element_by_class_name('proj-score')
                    # proj_awayscore = proj_score.find_element_by_class_name('one').text
                    # proj_homescore = proj_score.find_element_by_class_name('three').text

                    pick_value = data.find_element_by_class_name('pick-label').text.split('|')[0].strip()
                    value = data.find_element_by_class_name('value').text
                    light_pick = data.find_element_by_class_name('light-pick').text
                    simulation_percentage = data.find_element_by_class_name('simulation-label'). \
                        text.replace('SIMULATION:', '').replace('%', '').strip()
                    public_percentage = data.find_element_by_class_name('public-label'). \
                        text.replace('PUBLIC:', '').replace('%', '').strip()
                    title = data.find_element_by_class_name('title').text.strip()

                    sim_value = get_percentage_value(simulation_percentage)
                    pub_value = get_percentage_value(public_percentage)

                    if sim_value >= self.percentage and pub_value >= self.percentage:
                        if status == GAME_STATUS_FINAL:
                            score = driver.find_element_by_class_name('score')
                            awayscore = score.find_element_by_class_name('one').text
                            homescore = score.find_element_by_class_name('three').text
                            total_score = awayscore + homescore

                            if title == OVER_UNDER:
                                print hometeam, awayteam
                                print title
                                print pick_value, simulation_percentage, public_percentage, value, light_pick

                        elif title != MONEY_LINE:
                            print hometeam, awayteam
                            print title
                            print status
                            print pick_value, simulation_percentage, public_percentage, value, light_pick
                            print "---------------"

        except Exception as ex:
            print ex
            driver.close()
            driver.quit()

        driver.close()
        driver.quit()


def get_games(driver):
    game_data = dict()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'picksheet')))
    games = driver.find_elements_by_class_name('data-row')

    for game in games:
        game_status = game.find_element_by_class_name('top').text
        url = game.get_attribute('href')
        game_data[url] = {'game_status': game_status}

    return game_data


def get_percentage_value(value):
    try:
        return int(value)
    except ValueError:
        return 0

