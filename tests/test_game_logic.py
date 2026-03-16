import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

# --- update_score tests ---

def test_update_score_win_attempt_1():
    # Win on attempt 1: points = 100 - 10*(1+1) = 80
    result = update_score(0, "Win", 1)
    assert result == 80

def test_update_score_win_attempt_5():
    # Win on attempt 5: points = 100 - 10*(5+1) = 40
    result = update_score(0, "Win", 5)
    assert result == 40

def test_update_score_win_minimum_points():
    # Win on attempt 9: 100 - 10*10 = 0, but minimum is 10
    result = update_score(0, "Win", 9)
    assert result == 10

def test_update_score_win_adds_to_existing_score():
    # Win with existing score of 50, attempt 1: 50 + 80 = 130
    result = update_score(50, "Win", 1)
    assert result == 130

def test_update_score_too_high_deducts_5():
    result = update_score(100, "Too High", 1)
    assert result == 95

def test_update_score_too_low_deducts_5():
    result = update_score(100, "Too Low", 2)
    assert result == 95

def test_update_score_wrong_guess_from_zero():
    # Score can go negative
    result = update_score(0, "Too High", 1)
    assert result == -5

def test_update_score_unknown_outcome_no_change():
    result = update_score(42, "Unknown", 1)
    assert result == 42

