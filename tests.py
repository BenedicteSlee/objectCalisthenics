import main
import pytest

def test_team_with_correct_players():
    players = teamTestDataBuilder(4,4)
    main.Team(players)
    pass

def test_team_with_too_many__players_throws():
    players = teamTestDataBuilder(2,10)
    with pytest.raises(ValueError):
        main.Team(players)

def test_team_with_insufficient_players_throws():
    players = teamTestDataBuilder(4,1)
    with pytest.raises(ValueError):
        main.Team(players)

def test_team_with_insufficient_males_throws():
    players = teamTestDataBuilder(0,9)
    with pytest.raises(ValueError):
        main.Team(players)

def test_team_with_insufficient_females_throws():
    players = teamTestDataBuilder(7,1)
    with pytest.raises(ValueError):
        main.Team(players)

def teamTestDataBuilder(numberOfMalePlayers, numberOfFemalePlayers):
    players = [None] * (numberOfMalePlayers + numberOfFemalePlayers)
    for i in range(numberOfMalePlayers):
        players[i] = main.Male()

    for i in range(numberOfFemalePlayers):
        players[i + numberOfMalePlayers] = main.Female()
    return players



if __name__ ==  '__main__':
    test_team_with_correct_players()