#!/usr/bin/env python3

Goal = '''
to create prefix-lists in aws
Author: Pat@Maendeleolab
'''

#Module imports
import logging, sys, os, json
from datetime import datetime
from time import sleep

#Path to local home and user folder
FPATH = os.environ.get('ENV_FPATH')

#logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ',\
                    filename=FPATH+'/maendeleolab_prefixList/prefix_lists.log', level=logging.INFO)

#adding flexibility for regions
def region_id(name='us-east-1'):
    return name # e.g: 'us-east-1'

def verify_prefix_list(prefix_list_name, region='us-east-1'):
    ''' Verifies if prefix list name already exists '''
    try:
        output = os.popen('aws ec2 describe-managed-prefix-lists --filters Name=tag:Name,Values=' + prefix_list_name + ' --region '+ region).read()
        prefix_list_data = json.loads(str(output))
        #if len(prefix_list_data['PrefixLists']) > 0 and len(prefix_list_data['PrefixLists'][0]['PrefixListName']):
        if len(prefix_list_data['PrefixLists'][0]['PrefixListName']) > 0:
            print(prefix_list_name + ' already exists!')
            return 1
    except Exception as err:
        logging.info(f'Logging "verify_prefix_list" in prefix_lists.log: {err} in {region}...')
        print(f'Logging "verify_prefix_list" in prefix_lists.log: {err} in {region}...')

#gets prefix-list version
def get_prefix_list_version(value, region='us-east-1'):
    try:
        response = os.popen("aws ec2 describe-managed-prefix-lists --filters 'Name=prefix-list-name,Values=" + value + "' " + ' --region '+ region).read()
        prefix_list_data = json.loads(str(response))
        data = prefix_list_data['PrefixLists'][0]['Version']
        return str(data)
    except Exception as err:
        logging.info(f'Logging "get_prefix_list_version" in prefix_lists.log: {err} in {region}...')
        print(f'Logging "get_prefix_list_version" in prefix_lists.log: {err} in {region}...')
	
#creates prefix
def create_prefix_list(**kwargs):
    try:
        if verify_prefix_list(kwargs['PrefixName'], kwargs['Region']) == 1:
            pass
        else:
            os.system("aws ec2 create-managed-prefix-list \
                --address-family IPv4 \
                --max-entries 25 \
                --entries Cidr=" + kwargs['Cidr'] + ",Description=" + kwargs['Description'] + "\
                --prefix-list-name "+ kwargs['PrefixName'] + "\
                --region " + kwargs['Region'] + "\
                --tag-specifications 'ResourceType=prefix-list,Tags=[{Key=" + kwargs['tag_key'] + ",Value=" + kwargs['tag_value'] + "}]'"
            )
            print(f'Create prefix_list {kwargs["PrefixName"]} in {kwargs["Region"]}...')
            logging(f'Create prefix_list {kwargs["PrefixName"]} in {kwargs["Region"]}...')
    except Exception as err:
        logging.info(f'Logging "create_prefix_list" in prefix_lists.log: {err} in {kwargs["Region"]}...')
        print(f'Logging "create_prefix_list" in prefix_lists.log: {err} in {kwargs["Region"]}...')

#gets prefix-list id from any given prefix-list name
def get_prefix_list_id(value, region='us-east-1'):
    try:
        response = os.popen("aws ec2 describe-managed-prefix-lists --filters 'Name=prefix-list-name,Values=" + value + "' " + ' --region '+ region).read()
        prefix_list_data = json.loads(str(response))
        data = prefix_list_data['PrefixLists']
        for info in data:
            return info['PrefixListId']
    except Exception as err:
        logging.info(f'Logging "get_prefix_list_id" in prefix_lists.log: {err} in {region}...')
        print(f'Logging "get_prefix_list_id" in prefix_lists.log: {err} in {region}...')

#gets prefix-list entries from any given prefix-list name
def get_prefix_list_entries(value, region='us-east-1'):
    try:
        response = os.popen("aws ec2 get-managed-prefix-list-entries --prefix-list-id " + value + " " + ' --region '+ region).read()
        prefix_list_data = json.loads(str(response))
        data = prefix_list_data['Entries']
        cidr_list = [info['Cidr'] for info in data]
        return cidr_list
    except Exception as err:
        logging.info(f'Logging "get_prefix_list_entries" in prefix_lists.log: {err} in {region}...')
        print(f'Logging "get_prefix_list_entries" in prefix_lists.log: {err} in {region}...')


#adds prefix-list
def add_prefix_list(**kwargs):
    try:
        os.system("aws ec2 modify-managed-prefix-list \
            --prefix-list-id " + kwargs['PrefixId'] + "\
            --current-version " + kwargs['Version'] + "\
            --region " + kwargs['Region'] + "\
            --add-entries Cidr=" + kwargs['Cidr'] + ",Description=" + kwargs['Description']
        )
        print(f'Add prefix_list {kwargs["PrefixId"]} in {kwargs["Region"]}...')
        logging(f'Add prefix_list {kwargs["PrefixId"]} in {kwargs["Region"]}...')
    except Exception as err:
        logging.info(f'Logging "add_prefix_list" in prefix_lists.log: {err} in {kwargs["Region"]}...')
        print(f'Logging "add_prefix_list" in prefix_lists.log: {err} in {kwargs["Region"]}...')

#removes prefix-list
def remove_prefix_list(**kwargs):
    try:
        os.system("aws ec2 modify-managed-prefix-list \
                --prefix-list-id " + kwargs['PrefixId'] + "\
                --current-version " + kwargs['Version'] + "\
                --region " + kwargs['Region'] + "\
                --remove-entries Cidr=" + kwargs['Cidr'] + ",Description=" + kwargs['Description'] 
        )
    except Exception as err:
        logging.info(f'Logging "remove_prefix_list" in prefix_lists.log: {err} in {kwargs["Region"]}...')
        print(f'Logging "remove_prefix_list" in prefix_lists.log: {err} in {kwargs["Region"]}...')

#deletes prefix-list
def destroy_prefix_list(prefix_list_id, region='us-east-1'):
    try:
        os.system("aws ec2 delete-managed-prefix-list \
            --region " + region + "\
            --prefix-list-id " + prefix_list_id
        )
        logging(f'Add destroy_prefix_list {prefix_list_id} in {region}...')
    except Exception as err:
        print('Logging "destroy_prefix_list" to prefix_lists.log in {region}...')
        logging.info(f'Logging "destroy_prefix_list" {err} in {region}...')

def erase_prefix_list(region='us-east-1'):
    try:
        ''' Deletes all prefix list that do not have any dependencies '''
        output = os.popen('aws ec2 describe-managed-prefix-lists  --region ' + region).read()
        prefix_list_data = json.loads(str(output))
        for data in prefix_list_data['PrefixLists']:
            print(f'Delete erase_prefix_list: {data["PrefixListId"]}...')
            destroy_prefix_list(data['PrefixListId'], region=region)
            logging.info('Delete erase_prefix_list: ' + data['PrefixListId'] + ' in region: ' + region)

        new_data = json.dumps(data, indent=2)
        print(new_data)
    except Exception as err:
        logging.info(f'Logging "erase_prefix_list" {err} in {region}...')
        print('Logging "erase_prefix_list" to prefix_list.log in {region}...')

# --------------------------------------- End --------------------------------------

