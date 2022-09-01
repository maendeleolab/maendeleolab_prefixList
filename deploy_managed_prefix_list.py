#!/usr/bin/python3

from maendeleolab_lib import * 

#Variable lists
#maendeleolab_infra = ['us-east-1', 'us-west-2',]
maendeleolab_infra = ['us-east-2']

#creates the prefix-list
#NetworkDev1_Public
for region in maendeleolab_infra:
		create_prefix_list(
				Cidr=build_subnet.get_SubnetCidr('NetworkDev1_Pub_1a', region),
				Description='NetworkDev1_Pub_1a',
				PrefixName='NetworkDev1_Public',
				tag_key='Name',
				Region=region,
				tag_value='NetworkDev1_Public'
		)
		#adding additional entries to the prefix list above
		add_prefix_list(
				PrefixId=get_prefix_list_id('NetworkDev1_Public', region),
				Version=get_prefix_list_version('NetworkDev1_Public', region),
				Cidr=build_subnet.get_SubnetCidr('NetworkDev1_Pub_1b', region),
				Region=region,
				Description='NetworkDev1_Pub_1b'
		)

#NetworkDev1_Private
for region in maendeleolab_infra:
		create_prefix_list(
						Cidr=build_subnet.get_SubnetCidr('NetworkDev1_Priv_1a', region),
						Description='NetworkDev1_Priv_1a',
						PrefixName='NetworkDev1_Private',
						tag_key='Name',
						Region=region,
						tag_value='NetworkDev1_Private'
		)
		#adding entry to the prefix list above
		add_prefix_list(
						PrefixId=get_prefix_list_id('NetworkDev1_Private', region),
						Version=get_prefix_list_version('NetworkDev1_Private', region),
						Cidr=build_subnet.get_SubnetCidr('NetworkDev1_Priv_1b', region),
						Region=region,
						Description='NetworkDev1_Priv_1b'
		)

#This for loop is looping thru regions
for region in maendeleolab_infra:
		#SSH_From_Public
		create_prefix_list(
						Cidr='100.36.91.59/32', #This creates access from internet
						Description='Access_from_internet',
						PrefixName='SSH_From_Public',
						tag_key='Name',
						Region=region,
						tag_value='SSH_From_Public'
		)
		#RFC_1918
		create_prefix_list(
						Cidr='10.0.0.0/8', #This creates entry for 10.0.0.0/8
						Description='rfc_1918',
						PrefixName='rfc_1918',
						tag_key='Name',
						Region=region,
						tag_value='rfc_1918' 
		)
		add_prefix_list(
						PrefixId=get_prefix_list_id('rfc_1918', region),
						Version=get_prefix_list_version('rfc_1918', region),
						Cidr='172.16.0.0/12', #This creates entry for 172.16.0.0/12
						Region=region,
						Description='rfc_1918'
		)
		add_prefix_list(
					PrefixId=get_prefix_list_id('rfc_1918', region),
						Version=get_prefix_list_version('rfc_1918', region),
						Cidr='192.168.0.0/16', #This creates entry for 192.168.0.0/16
						Region=region,
						Description='rfc_1918'
		)

		#Default
		create_prefix_list(
				Cidr='0.0.0.0/0', #This creates entry for 0.0.0.0/0
				Description='Default_route',
				PrefixName='Default_route',
				tag_key='Name',
				Region=region,
				tag_value='Default_route' 
		)

internet_list = ['205.251.242.103/32','172.253.115.101/32','205.128.230.231/32','99.84.108.35/32','103.224.182.246/32',]
#This second loop is to add more entries to prefix list above "SSH_From_Public"
for region in maendeleolab_infra: #for each region in maendeleolab_infra list
	for ip in internet_list: #for ip addresses in internet_list
			add_prefix_list(
							PrefixId=get_prefix_list_id('SSH_From_Public', region),
							Version=get_prefix_list_version('SSH_From_Public', region),
							Cidr=ip,
							Region=region,
							Description='Access_from_internet'
			)

#Only use the syntax below, if you need to remove an entry.
#My advice is to do it from the console, unless you have a lot of places to touch.
#remove_prefix_list(
#				PrefixId=get_prefix_list_id('NetworkDev1_Public'),
#				Version=get_prefix_list_version('NetworkDev1_Public'),
#				Cidr='10.0.0.0/8',
#				Region=region_id("us-east-1"),
#				Description='NetworkDev1_route1'
#)
#

# ------------------------------------ End --------------------------------
