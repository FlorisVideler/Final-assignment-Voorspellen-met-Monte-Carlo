import numpy as np
from tabulate import tabulate


class Team:
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds
        self.check_probabilities()
        self.odds_as_list = self.probabilities_to_list()

    def check_probabilities(self):
        """Check if the probabilities are 100"""
        for i in self.odds:
            if sum(self.odds[i]) != 100:
                raise ValueError('Odds don\'t add up to 100 my g.')

    def probabilities_to_list(self):
        """0 = home win, 1 = draw, 2 = away win"""
        probabilities_as_list = {}
        for i in self.odds:
            odd_list = [0] * self.odds[i][0] + [1] * self.odds[i][1] + [2] * self.odds[i][2]
            probabilities_as_list[i] = odd_list
        return probabilities_as_list


class Tournament:
    def __init__(self, teams, n):
        self.teams = teams
        self.matches = []
        self.schedule_matches()
        self.results = self.init_results()
        self.n = n
        self.all_results = {}

    def init_results(self):
        results = {}
        for i in self.teams:
            results[i.name] = 0
        return results

    def schedule_matches(self):
        for i in self.teams:
            for j in self.teams:
                if i != j:
                    match = [i, j]
                    self.matches.append(match)

    def play_all_matches(self):
        for i in self.matches:
            home = i[0]
            away = i[1]
            self.play_match(home, away)

    def show_results(self):
        pass

    def play_match(self, home, away):
        # Voor nu nog ff np random
        result = home.odds_as_list[away.name][int(np.floor(np.random.rand() * 100))]
        if result == 0:
            self.results[home.name] += 3
        elif result == 1:
            self.results[home.name] += 1
            self.results[away.name] += 1
        else:
            self.results[away.name] += 3

    def batch_run(self):
        for i in range(self.n):
            self.play_all_matches()
            self.parse_results(i)
            self.results = self.init_results()

    def parse_results(self, run):
        tournament_result = {k: v for k, v in sorted(self.results.items(), key=lambda item: item[1], reverse=True)}
        self.all_results[run] = list(tournament_result.keys())

    def show_all_results(self):
        amount_of_tournaments_played = len(self.all_results)
        places = {}
        headers = []
        table = []

        for i in range(len(self.teams)):
            places[i] = []
            headers.append(f'{i+1}st pos')
        for i in self.all_results:
            for j in range(len(self.all_results[i])):
                places[j].append(self.all_results[i][j])

        # [['utrecht', 44%, 30%, 2%, 32%], ...]
        for i in self.teams:
            table_row = [i.name]
            for j in places:
                table_row.append(f'{round(places[j].count(i.name) / amount_of_tournaments_played * 100, 2)}%')
            table.append(table_row)
        print(f'After playing {amount_of_tournaments_played} tournaments this are the results:')
        print(tabulate(table, headers=headers))