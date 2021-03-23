## Object bidding

    The algorithm respects the conditions of a bidding and follows the next conditions:
    - if there are less than 2 competitors the bidding will not take place
    - there have to be at least 2 competitors bidding a higher price than the reserved price, 
    the bidding will not take place 
    
    The algorithm received a JSON as a input with the:
    - reservedPrice (integer/float)
    - potentialBuyersNumber (integer)
    - potentialBuyers which is a list of people which have:
        - the name (string)
        - the bids (list of integer/float)
        
    Functions:
    check_eligibility:
        - is checking if the algorithm can be applies on the data
        - returns a boolean value: True / False
    get_person_max_bid
        - returns the maximum value bidded by a person
    get_winner
        - returns the person who bidded the higher value
    get_won_price
        - returns the price that won the bidding
