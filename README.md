# maendeleolab_prefixList
![GitHub commit activity](https://img.shields.io/github/last-commit/maendeleolab/maendeleolab_prefixList)

<img src="/images/banner.png" width=400>

```
├── build_prefix_list.py
├── delete_resources.py
├── deploy_managed_prefix_list.py
├── maendeleolab_lib.py
└── prefix_lists.log
```

## [Context](#Context)

- This repo was built to create regional prefix lists. 

- It can be used on any Linux environment in AWS or on-premises. 

- Install Python 3.6.9 (or higher) and awscli version 2.

- The scripts are idempotent.

- The line above means, if the resource is tagged with a name that already exists, it will not create another one.

## [Prerequisites](#Prerequisites)

- Please watch the [requirements steps](https://www.youtube.com/watch?v=gMM-d1uZ0Ks&t=12s)

- It helps to be familiar with Linux basics commands.

- Must have awscli version 2 and Python 3.6.9 (or higher) installed.

- I recommend dedicating an instance (or on-premises server) to programmatically run the scripts.  

- Assign a role with programmatic access to the instance/server default profile.

- Run this command 'export ENV_FPATH="folder-path" ' 

- Replace folder-path with your folder location (this is the folder, where you will download the repo). 

See the example below.

```
export ENV_FPATH="/home/ubuntu"
```

## [Dependencies](#Dependencies)
### The deploy script needs to access the build script/s in the following project.

- [maendeleolab_subnet](https://github.com/maendeleolab/maendeleolab_subnet) 

## [Walk-through](#Walk-through)

**1**  - Make sure to comply with the prerequisites mentioned above.

**2**  - Update and install the latest packages of your Linux distribution system.

**3**  - Clone this repo to the instance/server using the syntax below.

```
git clone https://github.com/maendeleolab/maendeleolab_prefixList.git
```

**4**  - cd to folder maendeleolab_prefixList

```
cd maendeleolab_prefixList
```

**5**  - List the files in the folder with the **ls** command. It should match the files below.

**Note:** A file named **prefix_lists.log** will be created to store the scripts logs, when you run the script for the first time.

Remember to use it to monitor your environment or troubleshoot an issue.

```
README.md
LICENSE
images
build_prefix_list.py
delete_resources.py
deploy_managed_prefix_list.py
maendeleolab_lib.py
```

**6**  - I recommend running the script **deploy_managed_prefix_list.py** to see what the expected results look like.

The script will create prefix lists for the region, where you are deploying them to.

This script will become your single source of truth for your prefix lists. 

```
./deploy_managed_prefix_list.py or python3 deploy_managed_prefix_list.py
```

**7**  - Verify the expected results are present in the console. 

**8**  - Run the script again to verify idempotency is working as expected. 

**9**  - Prefix list resources do not cost you anything, but in case you decide to delete them. You can run the script **delete_resources.py**
	
**Note:** The script deletes all prefix lists resources that do not have any dependencies. 
	
This means, if the prefix list name is not associated to a VPC route table, security group or AWS network firewall rules, the prefix list will be deleted. 

```
./delete_resources.py or python3 delete_resources.py
```

**11** - If you get to this step, congratulations for being brave to do it! 

## [Support](#Support)
If you find this script useful, please support it with a shout out on your favorite social media platform!

![Twitter](https://img.shields.io/twitter/follow/maendeleolab?style=social)
```
Twitter : @maendeleolab
Instagram : @maendeleolab
TitTok : @pat_maendeleolab
```
## [License](#License)
GNU GENERAL PUBLIC LICENSE

	
