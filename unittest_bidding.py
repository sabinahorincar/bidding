import unittest
from bidding import check_eligibility, get_winner, get_won_price

input1 = {"A": [100, 130], "B": [], "C": [125], "D": [105, 115, 90], "E": [132, 135, 140]}
input2 = {"A": [], "B": [], "C": [], "D": [80, 90], "E": [55, 60, 70]}
input3 = {"A": [], "B": [], "C": [], "D": [80, 90], "E": []}

class TestBidding(unittest.TestCase):
    def test_check_eligibility(self):
        self.assertEqual(check_eligibility(100, input1), True, "Should be True")
        self.assertEqual(check_eligibility(500, input1), False, "Should be False")
        self.assertEqual(check_eligibility(100, input2), False, "Should be False")
        self.assertEqual(check_eligibility(50, input2), True, "Should be True")
        self.assertEqual(check_eligibility(50, input3), False, "Should be False")

    def test_get_winner(self):
        self.assertEqual(get_winner(input1), "E", "Should be E")
        self.assertEqual(get_winner(input2), "D", "Should be D")

    def test_get_won_price(self):
        self.assertEqual(get_won_price(input1, "E"), 130, "Should be 130")
        self.assertEqual(get_won_price(input2, "D"), 70, "Should be 70")

if __name__ == '__main__':
    unittest.main()
