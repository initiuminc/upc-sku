import json
input_file=raw_input("Enter the Input File :")
w=open('walgreens.upc', 'w', buffering=0)
upccodes=[]
if input_file:
  for line in open(input_file):
    data=json.loads(line)
    if data['upc']:
      w.write(data['upc']+ "\n")
