from bs4 import BeautifulSoup
from urllib import request
import names
import json
import os
import datetime
import random
import math

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
	amnt = loan["loanAmount"]
	currentDict = currentDict
	currentDict["num_loan"] += 1
	currentDict["total_borrowed"] += amnt
	if (completed == 0):
		currentDict["num_scams"] += 1
		currentDict["total_scammed"] += amnt
	if (completed == 1):
		currentDict["num_pending"] += 1
		currentDict["total_pending"] += amnt
	if (completed == 2):
		currentDict["num_repaid"] += 1
		currentDict["total_repaid"] += amnt
	return currentDict

def spoofData (scraped_data):
	d = scraped_data
	for bid, loans in list(d.items()): #bid = borrwer_id / borrower_username
		loans_temp = d[bid]
		d[bid] = {"loans":{}}
		for i in range(len(loans_temp)):
			d[bid]["loans"][i] = loans_temp[i]
		# d[bid]["loans"] = loans_temp

		borrower_info = {"num_loan":0, "num_repaid":0, "num_pending":0, "num_scams":0, "total_borrowed":0, "total_repaid":0, "total_pending":0, "total_scammed":0}
		for loan in loans:
			borrower_info = addLoanToDict(borrower_info, loan)
		percentage_scam = float(borrower_info["num_repaid"]) / borrower_info["num_loan"]
		print(d[bid])
		# spoof name
		d[bid]["first_name"] = names.get_first_name() 
		d[bid]["last_name"] = names.get_last_name() 

		# spoof age to be older if you have more repaid loans
		min_age = min(70, 15 + borrower_info["num_repaid"])
		d[bid]["age"] = random.randint(min_age, min_age + 10)

		# spoof education level correlated with what percent of loans a person has paid back
		percentage_scam = percentage_scam * 4
		d[bid]["education"] = max(0, math.floor(percentage_scam + random.uniform(-2, .25)))

		# Metric for estimating monthly income
		if (borrower_info["num_repaid"] != 0):
			monthly_income = borrower_info["total_repaid"] / borrower_info["num_repaid"] * 20
		else: 
			monthly_income = 0
		income_list = []
		for i in range(12): income_list.append(round(random.uniform(monthly_income - 0.05 * monthly_income, monthly_income + 0.05 * monthly_income)))
		d[bid]["monthly_income"] = tuple(income_list)

	return d

def transform_dict(dict_list):
	ret_dict = {}
	for borrower in dict_list:
		ret_dict[borrower['username']] = borrower['loans']
		for loan in ret_dict[borrower['username']]:
			loan['loanAmount'] = int(loan["loanAmount"][1:])
			# loan['dateLent'] = loan['dateLent'].strftime('%m-%d-%Y')
			# if loan['status'] == 2: 
			# 	loan['datePaid'] = loan['datePaid'].strftime('%m-%d-%Y')
			# else:
			# 	loan['datePaid'] = ""
			print(loan['datePaid'])
	return ret_dict



# dict_data = json.load(open("sample.json", 'r'))
dict_data = [{'loans': [{'borrower': 'makeshiftpatriot', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$150', 'datePaid': '', 'dateLent': '2018-01-09 03:22:11'}], 'username': 'makeshiftpatriot'}, {'loans': [{'borrower': 'iAmCrank310', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$150', 'datePaid': '2017-11-15 06:12:21', 'dateLent': '2017-10-29 22:34:50'}], 'username': 'iAmCrank310'}, {'loans': [{'borrower': 'jpwns93', 'status': 2, 'lender': 'keuraeyongpab', 'loanAmount': '$40', 'datePaid': '2016-02-21 02:12:34', 'dateLent': '2016-02-02 20:49:06'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'keuraeyongpab', 'loanAmount': '$75', 'datePaid': '2016-02-21 02:12:36', 'dateLent': '2016-02-10 00:36:22'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'saintsintosea', 'loanAmount': '$300', 'datePaid': '2016-05-05 15:56:02', 'dateLent': '2016-03-02 21:17:57'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'nicacio', 'loanAmount': '$225', 'datePaid': '2017-01-20 16:28:13', 'dateLent': '2016-12-01 15:20:33'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'nicacio', 'loanAmount': '$350', 'datePaid': '', 'dateLent': '2017-02-05 05:46:47'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'IgrewAtomato', 'loanAmount': '$150', 'datePaid': '2017-04-21 21:44:20', 'dateLent': '2017-02-27 18:20:54'}, {'borrower': 'jpwns93', 'status': 2, 'lender': '_cup_', 'loanAmount': '$750', 'datePaid': '2017-06-07 19:20:36', 'dateLent': '2017-04-27 00:52:39'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'gebraroest', 'loanAmount': '$60', 'datePaid': '2017-05-22 17:10:30', 'dateLent': '2017-05-14 18:23:26'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$500', 'datePaid': '2017-08-05 23:19:46', 'dateLent': '2017-05-24 15:04:18'}, {'borrower': 'jpwns93', 'status': 2, 'lender': '_cup_', 'loanAmount': '$225', 'datePaid': '2017-07-21 16:53:54', 'dateLent': '2017-06-07 20:29:24'}, {'borrower': 'jpwns93', 'status': 2, 'lender': '_cup_', 'loanAmount': '$120', 'datePaid': '2017-07-21 16:53:54', 'dateLent': '2017-06-09 18:15:58'}, {'borrower': 'jpwns93', 'status': 2, 'lender': '_cup_', 'loanAmount': '$420', 'datePaid': '2017-09-07 13:27:16', 'dateLent': '2017-07-26 03:52:04'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$145', 'datePaid': '2017-09-07 16:48:06', 'dateLent': '2017-08-11 23:23:45'}, {'borrower': 'jpwns93', 'status': 2, 'lender': '_cup_', 'loanAmount': '$110', 'datePaid': '2017-09-23 05:36:33', 'dateLent': '2017-08-27 03:40:24'}, {'borrower': 'jpwns93', 'status': 2, 'lender': '_cup_', 'loanAmount': '$40', 'datePaid': '2017-09-23 05:36:33', 'dateLent': '2017-08-31 15:38:48'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'IgrewAtomato', 'loanAmount': '$300', 'datePaid': '2017-10-06 17:22:08', 'dateLent': '2017-09-07 13:45:11'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$150', 'datePaid': '2017-10-20 17:51:13', 'dateLent': '2017-09-14 18:30:07'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$300', 'datePaid': '2017-10-20 17:51:13', 'dateLent': '2017-09-20 16:34:42'}, {'borrower': 'jpwns93', 'status': 2, 'lender': '_cup_', 'loanAmount': '$75', 'datePaid': '2017-10-06 14:50:05', 'dateLent': '2017-09-29 19:54:34'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'IgrewAtomato', 'loanAmount': '$275', 'datePaid': '2017-11-07 15:09:20', 'dateLent': '2017-10-04 16:25:08'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'HotelMoscow', 'loanAmount': '$80', 'datePaid': '2017-10-20 22:34:51', 'dateLent': '2017-10-18 03:37:23'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'HotelMoscow', 'loanAmount': '$250', 'datePaid': '2017-11-22 15:20:57', 'dateLent': '2017-10-21 23:19:10'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'IgrewAtomato', 'loanAmount': '$60', 'datePaid': '2017-11-23 00:39:47', 'dateLent': '2017-10-30 20:44:40'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$200', 'datePaid': '2017-12-07 16:08:31', 'dateLent': '2017-11-10 23:51:46'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'IgrewAtomato', 'loanAmount': '$40', 'datePaid': '2017-12-09 18:36:09', 'dateLent': '2017-11-15 06:18:58'}, {'borrower': 'jpwns93', 'status': 2, 'lender': '_cup_', 'loanAmount': '$600', 'datePaid': '2018-01-05 20:13:55', 'dateLent': '2017-11-25 07:57:26'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'MrMacgoot', 'loanAmount': '$320', 'datePaid': '', 'dateLent': '2017-12-04 18:48:24'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'ImNotFish', 'loanAmount': '$200', 'datePaid': '2018-01-09 19:37:00', 'dateLent': '2017-12-09 18:39:00'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'l80sman104', 'loanAmount': '$300', 'datePaid': '', 'dateLent': '2017-12-21 22:19:10'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'knotforhugh', 'loanAmount': '$175', 'datePaid': '2018-01-05 17:58:52', 'dateLent': '2017-12-26 00:48:31'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'txag09', 'loanAmount': '$28', 'datePaid': '2018-01-05 16:45:37', 'dateLent': '2018-01-04 03:47:16'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'txag09', 'loanAmount': '$400', 'datePaid': '', 'dateLent': '2018-01-05 20:45:46'}, {'borrower': 'jpwns93', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$450', 'datePaid': '', 'dateLent': '2018-01-10 21:54:42'}], 'username': 'jpwns93'}, {'loans': [{'borrower': 'Nixkels', 'status': 0, 'lender': 'OrlandoGallagher', 'loanAmount': '$125', 'datePaid': '', 'dateLent': '2017-11-08 00:11:28'}], 'username': 'Nixkels'}, {'loans': [{'borrower': 'JamesVista', 'status': 2, 'lender': 'williamtech814', 'loanAmount': '$40', 'datePaid': '2017-04-12 00:56:43', 'dateLent': '2017-04-01 20:11:33'}, {'borrower': 'JamesVista', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$40', 'datePaid': '2017-12-04 23:03:48', 'dateLent': '2017-12-01 18:18:59'}, {'borrower': 'JamesVista', 'status': 2, 'lender': 'Huizui', 'loanAmount': '$100', 'datePaid': '2018-01-06 02:36:15', 'dateLent': '2017-12-28 03:59:27'}], 'username': 'JamesVista'}, {'loans': [{'borrower': 'WarringBrood', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$60', 'datePaid': '2017-11-08 00:15:42', 'dateLent': '2017-11-01 21:39:42'}, {'borrower': 'WarringBrood', 'status': 2, 'lender': 'SuburbanMango', 'loanAmount': '$200', 'datePaid': '2017-12-14 19:55:58', 'dateLent': '2017-11-28 23:51:07'}], 'username': 'WarringBrood'}, {'loans': [{'borrower': 'JKaye57', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$250', 'datePaid': '2018-01-09 03:26:08', 'dateLent': '2017-12-08 01:28:50'}], 'username': 'JKaye57'}, {'loans': [{'borrower': 'shotofcourage', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$50', 'datePaid': '2017-10-30 21:08:59', 'dateLent': '2017-10-21 01:52:55'}, {'borrower': 'shotofcourage', 'status': 2, 'lender': 'elaboratexplanation', 'loanAmount': '$100', 'datePaid': '2017-11-08 07:11:16', 'dateLent': '2017-11-01 17:32:41'}, {'borrower': 'shotofcourage', 'status': 2, 'lender': 'mazdoore', 'loanAmount': '$100', 'datePaid': '2017-11-15 17:16:07', 'dateLent': '2017-11-09 19:19:02'}, {'borrower': 'shotofcourage', 'status': 2, 'lender': 'ryanplaya', 'loanAmount': '$50', 'datePaid': '2017-11-30 16:51:21', 'dateLent': '2017-11-29 14:42:10'}, {'borrower': 'shotofcourage', 'status': 2, 'lender': 'ryanplaya', 'loanAmount': '$300', 'datePaid': '2017-12-29 16:09:45', 'dateLent': '2017-12-11 17:13:06'}, {'borrower': 'shotofcourage', 'status': 2, 'lender': '_cup_', 'loanAmount': '$250', 'datePaid': '', 'dateLent': '2018-01-04 00:02:04'}], 'username': 'shotofcourage'}, {'loans': [{'borrower': 'NatorGator', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$100', 'datePaid': '2017-12-26 03:52:02', 'dateLent': '2017-10-21 21:15:39'}], 'username': 'NatorGator'}, {'loans': [{'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$75', 'datePaid': '2017-10-21 01:30:59', 'dateLent': '2017-10-12 17:46:51'}, {'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$30', 'datePaid': '2017-10-26 13:11:24', 'dateLent': '2017-10-22 22:19:00'}, {'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'DoctorCelebro', 'loanAmount': '$40', 'datePaid': '2017-11-08 13:57:28', 'dateLent': '2017-11-05 20:53:16'}, {'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'DoctorCelebro', 'loanAmount': '$95', 'datePaid': '2017-11-22 18:04:57', 'dateLent': '2017-11-18 23:05:04'}, {'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'DoctorCelebro', 'loanAmount': '$115', 'datePaid': '2017-12-06 15:14:52', 'dateLent': '2017-11-29 11:14:30'}, {'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$20', 'datePaid': '2017-12-23 06:36:37', 'dateLent': '2017-12-10 02:10:03'}, {'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'HotelMoscow', 'loanAmount': '$100', 'datePaid': '2018-01-04 23:01:20', 'dateLent': '2017-12-26 20:30:20'}, {'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'txag09', 'loanAmount': '$20', 'datePaid': '2018-01-03 16:36:20', 'dateLent': '2018-01-02 04:15:04'}, {'borrower': 'Kristen_hewa', 'status': 2, 'lender': 'txag09', 'loanAmount': '$200', 'datePaid': '', 'dateLent': '2018-01-04 04:21:01'}], 'username': 'Kristen_hewa'}, {'loans': [{'borrower': 'YungAshtray', 'status': 0, 'lender': 'OrlandoGallagher', 'loanAmount': '$150', 'datePaid': '', 'dateLent': '2017-10-23 02:56:58'}, {'borrower': 'YungAshtray', 'status': 0, 'lender': '1212thedoctor', 'loanAmount': '$75', 'datePaid': '', 'dateLent': '2017-10-24 22:21:20'}, {'borrower': 'YungAshtray', 'status': 0, 'lender': 'ricnus', 'loanAmount': '$75', 'datePaid': '', 'dateLent': '2017-10-27 04:22:51'}, {'borrower': 'YungAshtray', 'status': 0, 'lender': 'DoctorCelebro', 'loanAmount': '$75', 'datePaid': '', 'dateLent': '2017-10-29 03:27:55'}], 'username': 'YungAshtray'}, {'loans': [{'borrower': 'YesIHavwPTSD', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$50', 'datePaid': '2017-11-14 08:05:35', 'dateLent': '2017-10-23 03:11:58'}], 'username': 'YesIHavwPTSD'}, {'loans': [{'borrower': 'WhiteMoonOG', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$150', 'datePaid': '2017-12-01 15:42:40', 'dateLent': '2017-12-01 15:39:41'}], 'username': 'WhiteMoonOG'}, {'loans': [{'borrower': 'homicidoll', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$250', 'datePaid': '2017-10-20 12:56:16', 'dateLent': '2017-10-12 22:29:53'}, {'borrower': 'homicidoll', 'status': 2, 'lender': '_cup_', 'loanAmount': '$250', 'datePaid': '2017-11-03 08:17:04', 'dateLent': '2017-10-23 06:08:15'}, {'borrower': 'homicidoll', 'status': 2, 'lender': '_cup_', 'loanAmount': '$280', 'datePaid': '2017-11-20 11:12:13', 'dateLent': '2017-11-06 17:48:36'}, {'borrower': 'homicidoll', 'status': 2, 'lender': 'CVivien', 'loanAmount': '$175', 'datePaid': '2017-11-20 13:55:06', 'dateLent': '2017-11-15 16:25:49'}, {'borrower': 'homicidoll', 'status': 2, 'lender': 'orizinet', 'loanAmount': '$900', 'datePaid': '2017-12-20 23:22:35', 'dateLent': '2017-11-27 06:49:01'}, {'borrower': 'homicidoll', 'status': 2, 'lender': '_cup_', 'loanAmount': '$600', 'datePaid': '2018-01-06 05:03:54', 'dateLent': '2017-12-09 06:18:58'}, {'borrower': 'homicidoll', 'status': 2, 'lender': '_cup_', 'loanAmount': '$1000', 'datePaid': '', 'dateLent': '2018-01-11 16:01:38'}], 'username': 'homicidoll'}, {'loans': [{'borrower': 'yoginny', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$100', 'datePaid': '2017-12-23 06:44:25', 'dateLent': '2017-12-15 04:40:09'}], 'username': 'yoginny'}, {'loans': [{'borrower': 'le_fuque', 'status': 2, 'lender': 'thelocalproduction', 'loanAmount': '$100', 'datePaid': '2016-06-22 16:04:20', 'dateLent': '2016-06-19 19:38:25'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'hypermonkey2', 'loanAmount': '$300', 'datePaid': '2016-09-30 14:15:30', 'dateLent': '2016-08-29 19:19:05'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'MrMacgoot', 'loanAmount': '$500', 'datePaid': '2016-11-07 23:15:29', 'dateLent': '2016-10-08 17:02:34'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$600', 'datePaid': '2016-12-08 00:59:43', 'dateLent': '2016-11-08 01:29:57'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'MrMacgoot', 'loanAmount': '$500', 'datePaid': '2017-01-21 06:20:24', 'dateLent': '2016-12-09 20:32:30'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'Fabagemaf06', 'loanAmount': '$1100', 'datePaid': '2017-02-08 03:41:32', 'dateLent': '2017-01-27 02:47:16'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'Fabagemaf06', 'loanAmount': '$1000', 'datePaid': '2017-04-07 12:12:52', 'dateLent': '2017-03-01 02:17:02'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'danielcirca', 'loanAmount': '$2000', 'datePaid': '2017-11-08 00:12:37', 'dateLent': '2017-04-08 19:09:42'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$600', 'datePaid': '2017-10-08 15:53:22', 'dateLent': '2017-05-29 02:30:15'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$100', 'datePaid': '2017-11-23 00:13:09', 'dateLent': '2017-11-11 23:30:08'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$600', 'datePaid': '', 'dateLent': '2018-01-02 15:12:02'}, {'borrower': 'le_fuque', 'status': 2, 'lender': 'yoloswagmaster4jesus', 'loanAmount': '$200', 'datePaid': '', 'dateLent': '2018-01-09 01:02:31'}], 'username': 'le_fuque'}, {'loans': [{'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'dix86', 'loanAmount': '$50', 'datePaid': '2017-09-10 18:52:47', 'dateLent': '2017-08-31 19:20:18'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'dix86', 'loanAmount': '$170', 'datePaid': '2017-09-20 13:13:17', 'dateLent': '2017-09-10 19:30:19'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'dix86', 'loanAmount': '$260', 'datePaid': '2017-10-03 19:13:34', 'dateLent': '2017-09-27 14:21:05'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'dix86', 'loanAmount': '$265', 'datePaid': '2017-10-16 21:23:58', 'dateLent': '2017-10-05 23:49:28'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'dix86', 'loanAmount': '$265', 'datePaid': '2017-11-13 20:04:40', 'dateLent': '2017-10-19 01:37:24'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'dix86', 'loanAmount': '$265', 'datePaid': '2017-11-25 19:04:50', 'dateLent': '2017-11-13 23:22:34'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'Why_You_Always_Lying', 'loanAmount': '$225', 'datePaid': '2017-12-09 01:08:30', 'dateLent': '2017-11-29 16:16:11'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'dix86', 'loanAmount': '$850', 'datePaid': '', 'dateLent': '2017-12-02 23:52:21'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'Why_You_Always_Lying', 'loanAmount': '$265', 'datePaid': '', 'dateLent': '2017-12-19 01:50:56'}, {'borrower': 'Straight_Up_Turkey', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$250', 'datePaid': '', 'dateLent': '2018-01-10 04:11:36'}], 'username': 'Straight_Up_Turkey'}, {'loans': [{'borrower': '12px', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$30', 'datePaid': '2017-10-21 22:38:31', 'dateLent': '2017-10-15 17:08:28'}, {'borrower': '12px', 'status': 2, 'lender': 'ricnus', 'loanAmount': '$25', 'datePaid': '2017-11-28 15:04:45', 'dateLent': '2017-11-05 05:03:38'}], 'username': '12px'}, {'loans': [{'borrower': 'tharan1', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$75', 'datePaid': '2017-11-11 05:35:21', 'dateLent': '2017-11-01 00:56:51'}, {'borrower': 'tharan1', 'status': 0, 'lender': 'Jaxx666', 'loanAmount': '$125', 'datePaid': '', 'dateLent': '2017-12-04 00:18:50'}], 'username': 'tharan1'}, {'loans': [{'borrower': 'breakawayfl', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$80', 'datePaid': '2017-10-29 18:41:39', 'dateLent': '2017-10-17 05:06:30'}], 'username': 'breakawayfl'}, {'loans': [{'borrower': 'DeusEx-Machinist', 'status': 2, 'lender': 'rtwalz', 'loanAmount': '$20', 'datePaid': '2017-08-18 17:07:51', 'dateLent': '2017-08-17 16:09:28'}, {'borrower': 'DeusEx-Machinist', 'status': 2, 'lender': 'HotelMoscow', 'loanAmount': '$25', 'datePaid': '2017-09-22 15:26:42', 'dateLent': '2017-09-09 17:19:23'}, {'borrower': 'DeusEx-Machinist', 'status': 2, 'lender': 'HotelMoscow', 'loanAmount': '$100', 'datePaid': '2017-10-05 13:24:09', 'dateLent': '2017-09-22 16:10:51'}, {'borrower': 'DeusEx-Machinist', 'status': 2, 'lender': 'HotelMoscow', 'loanAmount': '$120', 'datePaid': '2017-10-20 22:45:47', 'dateLent': '2017-10-05 13:22:07'}, {'borrower': 'DeusEx-Machinist', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$100', 'datePaid': '2017-10-27 23:30:18', 'dateLent': '2017-10-15 23:35:45'}, {'borrower': 'DeusEx-Machinist', 'status': 2, 'lender': 'CVivien', 'loanAmount': '$400', 'datePaid': '', 'dateLent': '2017-10-31 22:17:07'}], 'username': 'DeusEx-Machinist'}, {'loans': [{'borrower': 'FreeKarmaReport', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$150', 'datePaid': '', 'dateLent': '2017-11-21 21:35:46'}], 'username': 'FreeKarmaReport'}, {'loans': [{'borrower': 'Liveinhermit', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$50', 'datePaid': '2017-10-26 13:21:36', 'dateLent': '2017-10-15 23:25:59'}, {'borrower': 'Liveinhermit', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$110', 'datePaid': '2017-11-11 05:31:37', 'dateLent': '2017-10-29 16:04:49'}, {'borrower': 'Liveinhermit', 'status': 2, 'lender': 'kashifr', 'loanAmount': '$110', 'datePaid': '2017-12-13 15:39:26', 'dateLent': '2017-11-13 16:45:24'}, {'borrower': 'Liveinhermit', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$110', 'datePaid': '2017-12-01 15:30:40', 'dateLent': '2017-11-21 20:47:54'}, {'borrower': 'Liveinhermit', 'status': 2, 'lender': 'OrlandoGallagher', 'loanAmount': '$150', 'datePaid': '', 'dateLent': '2017-12-04 15:13:06'}, {'borrower': 'Liveinhermit', 'status': 2, 'lender': 'Jaxx666', 'loanAmount': '$250', 'datePaid': '', 'dateLent': '2017-12-13 09:51:38'}, {'borrower': 'Liveinhermit', 'status': 2, 'lender': 'Rvatistanac', 'loanAmount': '$175', 'datePaid': '', 'dateLent': '2018-01-11 16:35:57'}], 'username': 'Liveinhermit'}]
dict_data = transform_dict(dict_data)
spoofed = spoofData(dict_data)
print(type(spoofed))
print(spoofed)

with open('spoofed_data.txt', 'w') as outfile:
    json.dump(spoofed, outfile)

		
"""

userid:{list of loans}

Out:
- Name
- Age
- Education (0 = None, 1 = High School, 2 = Bachelors, 3 = Masters)


"""