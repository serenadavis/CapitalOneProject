from bs4 import BeautifulSoup
from urllib import request
import names
import json


"""

Each loan information will have:
- Loanee ID
- Amount Borrowed
- completed
	0: Unpaid/Scam
	1: Pending
	2: Finished

Profile:
- Name
- Age
- Education

"""



def addLoanToDict (currentDict, loan):
	"""
	return dictionary with key id and values:
	- number of loans
	- number of scams
	- number finished
	- number pending
	- total amount ever borrowed
	- total amount repaid
	- total amount scammed 
	"""
	completed = loan["status"]
	amnt = loan["loanAmmount"]
	client = currentDict
	client["num_loan"] += 1
	client["total_borrowed"] += tup[amount_index]
	if (completed == 0):
		client["num_scams"] += 1
		client["total_scammed"] += amnt
	if (completed == 1):
		client["num_pending"] += 1
		client["total_pending"] += amnt
	if (completed == 2):
		client["num_repaid"] += 1
		client["total_scammed"] += amnt
	return clients

def spoofData (scraped_data):
	d = scraped_data
	for bid, loans in dictForm.iteritems(): #bid = borrwer_id / borrower_username
		borrower_info = {"num_loan":0, "num_repaid":0, "num_pending":0, "num_scam":0, "total_borrowed":0, "total_repaid":0, "total_pending":0, "total_scammed":0}
		for loan in loans:
			borrower_info = addLoanToDict(borrower_info, loan)
		percentage_scam = float(borrower_info["num_repaid"]) / borrower_info["num_loan"]
		
		# spoof name
		d[bid]["name"] = names.get_random_name() 

		# spoof age to be older if you have more repaid loans
		min_age = min(70, 15 + borrower_info["num_repaid"])
		d[bid]["age"] = random.randint(min_age, min_age + 10)

		# spoof education level correlated with what percent of loans a person has paid back
		percentage_scam = percentage_scam * 4
		d[bid]["education"] = min(0, Math.floor(percentage_scam + random.uniform(-1.00, .25)))

		# Metric for estimating monthly income
		monthly_income = borrower_info["total_repaid"] / borrower_info["num_repaid"] * 10
		income_list = []
		for i in range(12): income_list.append(Math.round(random.uniform(monthly_income - 0.05 * monthly_income, monthly_income + 0.05 * monthly_income)))
		d[bid]["monthly_income"] = tuple(income_list)


dict_data json.load("path")
spoofed = spoofData(dict_data)
with open('spoofed_data.txt', 'w') as outfile:
    json.dump(spoofed, outfile)

		

"""

userid:{list of loans}

Out:
- Name
- Age
- Education (0 = None, 1 = High School, 2 = Bachelors, 3 = Masters)



"""