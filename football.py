import numpy as np
from tabulate import tabulate


class Team:
    def __init__(self, name: str, odds: dict):
        """
        Initiator for the Team class

        :param name: str
            The name of the team
        :param odds: dict
            A dict with the odds for all the teams
        """
        self.name = name
        self.odds = odds
        self.check_probabilities()
        self.odds_as_list = self.probabilities_to_list()

    def check_probabilities(self):
        """
        Check if the odds add up to 100%
        """
        for i in self.odds:
            if sum(self.odds[i]) != 100:
                raise ValueError('Odds don\'t add up to 100 my g.')

    def probabilities_to_list(self) -> dict:
        """
        Put the odds in a list.
        Home win = 0
        Draw = 1
        Away win = 2

        :return: dict
            dict with lists with chances.
        """
        probabilities_as_list = {}
        for i in self.odds:
            odd_list = [0] * self.odds[i][0] + [1] * self.odds[i][1] + [2] * self.odds[i][2]
            probabilities_as_list[i] = odd_list
        return probabilities_as_list


class Tournament:
    def __init__(self, teams: list, n: int, rng):
        """
        Initiator for the Tournament class

        :param teams: list
            A list with team objects
        :param n: int
            How many times do you want to run the tournaments
        :param rng: random number generator
            A object to generate random numbers
        """
        self.teams = teams
        self.matches = []
        self.schedule_matches()
        self.results = self.init_results()
        self.n = n
        self.all_results = {}
        self.all_goal_diff = {}
        self.rng = rng

    def init_results(self) -> dict:
        """
        Rest the result object

        :return: dict
            Empty dict with team names
        """
        results = {}
        for i in self.teams:
            results[i.name] = 0
        return results

    def schedule_matches(self):
        """
        Make all the match combinations
        """
        for i in self.teams:
            for j in self.teams:
                if i != j:
                    match = [i, j]
                    self.matches.append(match)

    def play_all_matches(self):
        """
        Function to play all the matches
        """
        for i in self.matches:
            home = i[0]
            away = i[1]
            self.play_match(home, away)

    def play_match(self, home: Team, away: Team):
        """
        Play match

        :param home: Team
            The team that plays home
        :param away: Team
            The team that plays away
        """
        result = home.odds_as_list[away.name][self.rng.randomly()]
        # 0 = Home win
        # 1 = Draw
        # 2 (else) = Away wins
        if result == 0:
            self.results[home.name] += 3
        elif result == 1:
            self.results[home.name] += 1
            self.results[away.name] += 1
        else:
            self.results[away.name] += 3

    def batch_run(self):
        """
        Setup and run the batch run.
        """
        for i in range(self.n):
            self.play_all_matches()
            self.parse_results(i)
            self.results = self.init_results()

    def parse_results(self, run: int):
        """
        Parse the tournament results

        :param run: int
            The run number
        """
        tournament_result = {k: v for k, v in sorted(self.results.items(), key=lambda item: item[1], reverse=True)}
        self.all_results[run] = list(tournament_result.keys())

    def show_all_results(self):
        """
        Function to show all the results
        """
        amount_of_tournaments_played = len(self.all_results)
        places = {}
        headers = []
        table = []

        for i in range(len(self.teams)):
            places[i] = []
            headers.append(f'{i + 1}st pos')
        for i in self.all_results:
            for j in range(len(self.all_results[i])):
                places[j].append(self.all_results[i][j])

        # [['utrecht', 44%, 30%, 2%, 32%], ...]
        for i in self.teams:
            table_row = [i.name]
            for j in places:
                table_row.append(f'{round(places[j].count(i.name) / amount_of_tournaments_played * 100, 2)}%')
            table.append(table_row)
        print(
            f'After playing {amount_of_tournaments_played} tournaments using the {self.rng.name} this are the results:')
        print(tabulate(table, headers=headers))
        print('\n')
