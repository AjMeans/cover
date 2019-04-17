from multiprocessing import Process
from sport import Sport
from driver import Driver
import config


class OddsGenerator(object):

    def __init__(self, args):
        self.arguments = args

    def generate_best_odds(self):

        for key, value in vars(self.arguments).iteritems():
            if isinstance(value, bool) and value:
                sport = key.upper()
                # Initialize the driver
                driver = Driver()
                # Login
                driver.login(config.SPORT[sport]['URL'])
                # Initialize the Sport class
                sport_class = Sport(sport, self.arguments.percentage)
                sport_class.get_simulated_data(driver.driver)

        """
        if self.args.college_fball or self.args.all:
            # College Football
            college_fball_data = Process(target=self.get_sport_data, args=(config.COLLEGE_FBALL_URL,))
            college_fball_data.start()

        if self.args.nhl or self.args.all:
            # NHL
            nhl_data = Process(target=self.get_sport_data, args=(config.NHL_URL,))
            nhl_data.start()

        if self.args.nba or self.args.all:
            # NBA
            nba_data = Process(target=self.get_sport_data, args=(config.NBA_URL,))
            nba_data.start()

        if self.args.college_bball or self.args.all:
            # College Basketball
            college_bball_data = Process(target=self.get_sport_data, args=(config.COLLEGE_BBALL_URL,))
            college_bball_data.start()

        if self.args.nfl or self.args.all:
            # NFL
            nfl_data = Process(target=self.get_sport_data, args=(config.NFL_URL,))
            nfl_data.start()

        def get_sport_data(url):
            # Initialize the driver
            driver = Driver()
            # Login
            driver.login(url)
            # Initialize the Sport class
            sport = Sport()
            sport.get_data(driver.driver)
        """
