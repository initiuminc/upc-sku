import json
from requests import post

upc_codes=[]
input_file=raw_input("Enter the Input File with the extracted UPC No:")
with open(input_file.strip(), 'r') as f:
   upc_codes= [line.rstrip('\n') for line in f]

print "Total Number of Products ="  + str(len(upc_codes))
data={u'act': u'barcodeUPC',
   u'affId': u'photon',
   u'apiKey': u'd12ddc87a36f1cfb422dccb4ff0a7184',
   u'appver': u'4.0',
   u'atkn': u'mo/PxnoVq4ugQ3oRJ4ZZ8PHAdwo=',
   u'devinf': u'iPhone4,1',
   u'lat': u'',
   u'lng': u'',
   u'srl': u'4633',
   u'storeNum': u'',
   u'transId': u'2DD1749F-0119-497C-9A74-289DDBE57CC5',
   u'upcNo': u'9781573241984',
   u'view': u'barcodeJSON'}

url=  'https://services.walgreens.com/api/products/details'

upc_sku={}
j_d=open("upc_sku.txt",'w')
for upc in upc_codes:
  data[u'upcNo']= upc
  r = post(url=url, data=json.dumps(data))
  output=json.loads(r.content)
  if not 'errCode' in output:
    print "Found Sku for UPC -" + upc + " "    
    sku= output[u'productInfo'][u'sku_id']
    upc_sku[str(upc)]=str(sku)
    json.dump(upc_sku, j_d)
  else : print "Sku for UPC -" + upc + " Not Found"

