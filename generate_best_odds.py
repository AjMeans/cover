import argparse
from odds_generator import OddsGenerator

import config


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to grab game predictions')
    parser.add_argument('--nba', action='store_true')
    parser.add_argument('--nfl', action='store_true')
    parser.add_argument('--nhl', action='store_true')
    parser.add_argument('--college_fball', action='store_true')
    parser.add_argument('--college_bball', action='store_true')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--percentage', type=int, default=70)
    args = parser.parse_args()

    try:
        odds_generator = OddsGenerator(args)
        odds_generator.generate_best_odds()

    except Exception as ex:
        print "Exception occurred..."
        print ex
