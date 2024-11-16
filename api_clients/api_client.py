import requests

crudeCrudApi = 'http://192.168.110.143/phpcrudecrud/findemployee.php?lastname='

# Ask user for input:

lastName = input("Enter the Last Name to search for: ")

apiResponse = requests.get(crudeCrudApi + lastName)

print(apiResponse.text)