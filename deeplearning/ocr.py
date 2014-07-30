import Image
import os
import csv
import urllib, cStringIO
from sys import argv
from pytesseract import image_to_string
import barcode_reader as bc
import pdb, sys


def get_url_from_csv():
	file_name = argv[1]
	output_file = str.split(file_name,".")[0] + "_output.tsv"
	print output_file
	tsv_file = csv.DictReader(open(file_name, 'rb'), delimiter = '\t')
	#pdb.set_trace()
	header_name = tsv_file.fieldnames + ["ticket_number_ocr", "status"]
	writer = csv.writer(open( output_file, 'wt'), delimiter = '\t', quotechar = '', quoting = csv.QUOTE_NONE)
	writer.writerow(header_name)

	for row in tsv_file:
		print "==========================================="
		raw_url = row.get("ticket_number_url")
		print raw_url
		ocr_value = ['']
		barcode_value = None

		url = get_url(raw_url)
		if url:
			ocr_value = ocr(url)

		url = get_url(raw_url)
		if url:
			barcode_value = bc.main(url)

		print [ocr_value, barcode_value]
		print "*****************************"
		print get_correct_number(ocr_value, barcode_value)
		ocr_ticket_value = get_correct_number(ocr_value, barcode_value)
		#pdb.set_trace()
		writer.writerow(  [ row.get(x) for x in header_name[0:8]] + [ ocr_ticket_value['value'], ocr_ticket_value['status']])

def get_url(raw_url):
	url = None 
	try:
		url = cStringIO.StringIO(urllib.urlopen(raw_url).read())
	except Exception as e:
		print str(e)

	return url

def ocr(url):
	#print "***************", url , "****************"
	string = ['']
	try:
		string = str.split(image_to_string(Image.open(url)), "\n")
	except Exception as e:
		print str(e)

	return string

def get_correct_number(ocr_value, barcode_value):
	#pdb.set_trace()
	if barcode_value:
		return {"value":barcode_value, "status":1}
	elif ocr_value:
		return {"value":ocr_value[0], "status":2}
	else:
		return {"value":ocr_value[0], "status":0}


if __name__ == "__main__":
	get_url_from_csv()

