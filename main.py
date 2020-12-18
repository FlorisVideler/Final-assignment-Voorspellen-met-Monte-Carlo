from football import *
from randomly import *

ODDS = {
    'Ajax': {
        'Feyenood': [65, 17, 18],
        'PSV': [54, 21, 25],
        'FC Utrecht': [74, 14, 12],
        'Willem II': [78, 13, 9]
    },
    'Feyenood': {
        'Ajax': [30, 21, 49],
        'PSV': [37, 24, 39],
        'FC Utrecht': [51, 22, 27],
        'Willem II': [60, 21, 19]
    },
    'PSV': {
        'Ajax': [39, 22, 39],
        'Feyenood': [54, 22, 24],
        'FC Utrecht': [62, 20, 18],
        'Willem II': [62, 22, 16]
    },
    'FC Utrecht': {
        'Ajax': [25, 14, 61],
        'Feyenood': [37, 23, 40],
        'PSV': [29, 24, 47],
        'Willem II': [52, 23, 25]
    },
    'Willem II': {
        'Ajax': [17, 18, 65],
        'Feyenood': [20, 26, 54],
        'PSV': [23, 24, 53],
        'FC Utrecht': [37, 25, 38]
    }
}

GOALS = {
    'Ajax': {
        'HS': 3.2,
        'HC': 0.9,
        'AS': 3.1,
        'AC': 0.6
    },
    'Feyenood': {
        'HS': 2.4,
        'HC': 1.1,
        'AS': 2.2,
        'AC': 0.8
    },
    'PSV': {
        'HS': 2.1,
        'HC': 0.7,
        'AS': 1.8,
        'AC': 1.3
    },
    'FC Utrecht': {
        'HS': 1.9,
        'HC': 1.2,
        'AS': 3,
        'AC': 2.4
    },
    'Willem II': {
        'HS': 1.4,
        'HC': 1.7,
        'AS': 1,
        'AC': 1.5
    }
}

# make teams
teams = []
for i in ODDS:
    t = Team(i, ODDS[i], GOALS[i])
    teams.append(t)

tour = Tournament(teams, 10000, NumpyRandomly())
tour.batch_run()
tour.show_all_results()
tour = Tournament(teams, 10000, MiddleSquare())
tour.batch_run()
tour.show_all_results()
tour = Tournament(teams, 10000, LCG())
tour.batch_run()
tour.show_all_results()
tour = Tournament(teams, 10000, Mersenne())
tour.batch_run()
tour.show_all_results()