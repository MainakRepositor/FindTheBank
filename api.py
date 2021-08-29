import requests

## Making request to API
url = 'https://ifsc.razorpay.com/' + 'SBIN0000813' ## Any IFSC
bank_info = requests.get(url).json()
## Creating list for storing the data.
all_details = []
# Fetching information from the stored Json
bank_name = bank_info['BANK']
branch = bank_info['BRANCH']
address = bank_info['ADDRESS']
city = bank_info['CITY']
state = bank_info['STATE']
ifsc = bank_info['IFSC']
contact = bank_info['CONTACT']
## Putting Available & not available instead of true & false
upi = 'UPI: ' + 'Available' if bank_info['UPI'] == True else 'Not Available'
rtgs = 'RTGS: ' + 'Available' if bank_info['RTGS'] == True else 'Not Available'
neft = "NEFT: " + 'Available' if bank_info['NEFT'] == True else 'Not Available'
imps = 'IMPS: ' + 'Available' if bank_info['IMPS'] == True else 'Not Available'

all_details.append(bank_name)
all_details.append(branch)
all_details.append(address)
all_details.append(city)
all_details.append(state)
all_details.append(ifsc)
all_details.append(contact)
all_details.append(upi)
all_details.append(rtgs)
all_details.append(neft)
all_details.append(imps)

# Printing the all information
print(all_details)