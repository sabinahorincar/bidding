import json

def check_eligibility(price, buyers_dictionary):
    eligibility = False
    buyers = 0
    new_buyers_dictionary = {}
    for key, value in buyers_dictionary.items():
        new_buyers_dictionary[key] = []
        for v in value:
            if v >= price:
                eligibility = True
        
        if eligibility:
            buyers += 1
        if buyers >= 2:
            break
        eligibility = False

    return True if buyers >= 2 else False

def get_person_max_bid(values):
    return 0 if values == [] else max(values)

def get_winner(buyers_dictionary):
    max_bid = 0
    name = ''
    for key, values in buyers_dictionary.items():
        max_bid_of_person = get_person_max_bid(values)
        if max_bid < max_bid_of_person:
            max_bid = max_bid_of_person
            name = key
    return name

def get_won_price(buyers_dictionary, winner):
    won_price = 0
    filtered_buyers_dict = {key:value for (key, value) in buyers_dictionary.items() if key != winner}
    
    for key, values in filtered_buyers_dict.items():
        max_bid_of_person = get_person_max_bid(values)
        if won_price < max_bid_of_person:
            won_price = max_bid_of_person
    return won_price

def main():
    buyers_dictionary = {}
    reserved_price = 0

    with open('input.json') as json_file:
        data = json.load(json_file)
        reserved_price = data['reservedPrice']

        for buyer in data['potentialBuyers']:
            buyers_dictionary[buyer['name']] = buyer['bids']

    if not check_eligibility(reserved_price, buyers_dictionary):
        print("The bidding has failed")
        return
    
    winner = get_winner(buyers_dictionary)
    price = get_won_price(buyers_dictionary, winner)
    print("The winner:", winner, "&", "Winning price:",price)

if __name__ == "__main__":
    main()
    