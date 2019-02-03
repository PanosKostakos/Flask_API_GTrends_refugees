from __future__ import print_function
import sys
import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':sys.argv[1],})
print(r.json())