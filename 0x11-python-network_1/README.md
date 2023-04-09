0x11. Python - Network #1
- Python
- Scripting
- Back-end
- API

#### How to fetch internet resources with the Python package urllib
	- You can fetch internet resources with the package urllib by:
		- Importing the module `from urllib import request` and then defining the URL of the resource `url = "https://example.com". Using the urlopen() from the request module to open the URL `response = request.urlopen(url)` reading the content using read() method `contents = response.read()

#### How to decode urllib body response
	- To decode the body response of a urllib request, you can use the decode() method to convert the bytes object returned by the read() method into a string object. You can specify the character encoding of the response, if it is not already specified in the response header, by passing the encoding as a parameter to the decode() method.

#### How to use the Python package requests #requestsiswaysimplerthanurllib
	- The requests package is a popular and user-friendly Python library for making HTTP requests. Compared to urllib, requests is simpler to use and provides more convenient features out of the box.

#### How to make HTTP GET request
	- To make an HTTP GET request in Python, you can use the requests package

#### How to make HTTP POST/PUT/etc. request
	- To make an HTTP POST/PUT/DELETE/etc. request in Python using the requests package, you can use the corresponding method of the requests module, such as post(), put(), delete(), etc.

#### How to fetch JSON resources
	- To fetch JSON resources in Python using the requests package, you can make an HTTP GET request to the JSON resource URL and use the json() method of the response object to convert the response to a Python object.

#### How to manipulate data from an external service
	- To manipulate data from an external service in Python, you typically need to fetch the data from the service using an API or a web scraping technique, then process the data as needed using Python code.
