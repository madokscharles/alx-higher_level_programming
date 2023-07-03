## 0x11. Python - Network #1

## How to fetch internet resources with the Python package urllib:
You can use the urllib.request module from the urllib package to fetch internet resources. The urlopen() function allows you to open URLs and retrieve the response.

## How to decode urllib body response:
The urlopen() function from urllib.request returns a response object. You can use the read() method to retrieve the response body as bytes. To decode the response into a string, you can use the decode() method with the appropriate encoding.

## How to use the Python package requests:
The requests package provides a higher-level interface for making HTTP requests compared to urllib. It simplifies the process and provides additional features. You can install requests using pip install requests.

## How to make an HTTP GET request:
With requests, you can make an HTTP GET request using the requests.get() method. You provide the URL as an argument, and the method returns a response object that contains the server's response.

## How to make an HTTP POST/PUT/etc. request:
Similarly, you can make other types of requests like POST, PUT, DELETE, etc., using the respective methods provided by requests, such as requests.post(), requests.put(), requests.delete(), etc. You pass the URL, data, headers (if required), and any other parameters as needed.

## How to fetch JSON resources:
You can use requests to fetch JSON resources by making an HTTP GET request to the URL that returns JSON data. The response object's json() method can be used to deserialize the JSON response into a Python object (e.g., a dictionary or a list).

## How to manipulate data from an external service:
Once you have fetched data from an external service, you can manipulate it using Python's built-in data manipulation capabilities. You can extract, filter, transform, and analyze the data using libraries like pandas or by writing your own Python code.
