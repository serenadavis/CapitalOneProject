import requests
from bs4 import BeautifulSoup
import datetime
import json, time

borrowerID = [8962, 6403, 3587, 7825, 5267, 7847, 7858, 7738, 7745, 6728, 7760, 7761, 8145, 7635, 8530, 4310, 7256, 7654, 6630, 4075, 7150, 8053, 6775]
entireDataList = []
#{"username":username,"Loans": [{"lender":x,"borrower":x,"loanAmount":x,"dateLent":x,"datePaid":x, "status":x}] }

for userID in borrowerID:
	extractedUserData = {}
	extractedUserData['username'] = ""
	extractedUserData['loans'] = []
	offset = 0
	while True: # loop to keep increasing pages
		url = "https://redditloans.com/mobile_query.php?checkid={}&limit=25&offset={}".format(userID, offset)
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		loans = soup.find_all('tr')
		if len(loans) > 1: # If there are loans on this page continue
			for loan in loans: # iterate through all loans
				dataColumns = loan.find_all('td')
				if len(dataColumns) > 0: # if 'loan' is actually a loan
					loanTuple = {}
					loanTuple['lender'] = dataColumns[2].text
					loanTuple['borrower'] = dataColumns[4].text
					loanTuple['loanAmount'] = dataColumns[5].text
					if dataColumns[7].text == "Yes":
						loanTuple['status'] = 0
					else:
						loanTuple['status'] = 2
					loanTuple['dateLent'] = dataColumns[8].text
					try:
						loanTuple['datePaid'] = dataColumns[9].text
					except: # no date of repayment
						loanTuple['status'] = 1
						loanTuple['datePaid'] = 0

					extractedUserData['loans'].append(loanTuple)

			offset += 25
		else:
			break
	extractedUserData['username'] = loanTuple['borrower']
	entireDataList.append(extractedUserData)
	time.sleep(5)


with open("scrapedData.txt", "a") as theFile:
	theFile.write(str(entireDataList))
