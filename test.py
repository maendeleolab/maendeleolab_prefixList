#!/usr/bin/python3
import os, json

response = os.popen("aws ec2 get-managed-prefix-list-entries --prefix-list-id pl-09f038e29531c2eb9").read()
prefix_list_data = json.loads(str(response))
data = prefix_list_data['Entries']
print(data)
for info in data:
  print(info['Cidr'])
