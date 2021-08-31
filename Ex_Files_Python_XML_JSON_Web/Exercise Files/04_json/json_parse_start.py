# Process JSON data returned from a server

# TODO: use the JSON module
import json

def main():
    # define a string of JSON code
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price" : 8.99
        }'''

    # TODO: parse the JSON data using loads
    data = json.loads(jsonStr)
    
    # TODO: print information from the data structure
    print("Sandwich " + data['sandwich'])
    for topping in data['toppings']:
        print('Topping is： ' + topping)

if __name__ == "__main__":
    main()
