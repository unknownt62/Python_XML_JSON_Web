# Send data to a server using urllib

# TODO: import the request and parse modules
import urllib.request
import urllib.parse

def main():
    url = "http://httpbin.org/get"

    # TODO: create some data to pass to the GET request
    args = {
        "name": "Mingze Ma",
        "is_fool": False
    }

    # TODO: the data needs to be url-encoded before passing as arguments
    data = urllib.parse.urlencode(args)

    # TODO: issue the request with the data params as part of the URL
    result = urllib.request.urlopen(url+"?"+data) # Used for get command

    # TODO: issue the request with a data parameter to use POST
    url_2 = "http://httpbin.org/post"
    data_2 = data.encode() # This encode is used to encode the string to bytes before sending data over
    result_2 = urllib.request.urlopen(url_2, data=data_2)

    print("Result code: {0}".format(result_2.status))
    print("Returned data: ----------------------")
    print(result_2.read().decode("utf-8"))


if __name__ == "__main__":
    main()
