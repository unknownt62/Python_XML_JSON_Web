# Process JSON data returned from a server

# use the JSON module
import json
from json import JSONDecodeError

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

    # parse the JSON data using loads
    try:
        data = json.loads(jsonStr)

        # print information from the data structure
        print("Sandwich: " + data['sandwich'])
        if (data['toasted']):
            print("And it's toasted!")
        for topping in data['toppings']:
            print("Topping: " + topping)
    except JSONDecodeError as err:
        print(f"Error msg is： {err.msg}")


if __name__ == "__main__":
    main()
