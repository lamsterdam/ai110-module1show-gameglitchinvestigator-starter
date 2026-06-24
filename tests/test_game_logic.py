import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from logic_utils import check_guess

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

def test_too_high_hint():
    # Guess of 50 with secret of 30: outcome should be "Too High" and hint should say Go LOWER
    outcome, message = check_guess(50, 30)
    assert outcome == "Too High"
    assert "LOWER" in message
