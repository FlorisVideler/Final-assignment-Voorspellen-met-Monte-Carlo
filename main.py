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

# make teams
teams = []
for i in ODDS:
    t = Team(i, ODDS[i])
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