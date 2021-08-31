# using urllib to request data

# TODO: import the urllib request class
import urllib.request

def main():
    # the URL to retrieve our sample data from 
    url = "http://httpbin.org/xml"

    # TODO: open the URL and retrieve some data
    result = urllib.request.urlopen(url)

    # TODO: Print the result code from the request, should be 200 OK


    # TODO: print the returned data headers
    print("Headers: ----------------------")
    print(f"Result code: {result.status}")

    # TODO: print the returned data itself
    print("Returned data: ----------------------")
    

if __name__ == "__main__":
    main()
