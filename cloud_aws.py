import boto3
client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')

### 1번.list_instance 함수

def list_instance() :
	instance_ids = []
	number = 1
	response = client.describe_instances()
	instances_full_details = response['Reservations']
	for instance_detail in instances_full_details:
        	group_instances = instance_detail['Instances']
        	for instance in group_instances:
        		print("[id] " + instance['InstanceId'], "[AMI] " + instance['ImageId'], "[type] " + instance['InstanceType'],
        		 "[state] " + instance['State']['Name'], "[monitoring state] " + instance['Monitoring']['State'])
            		
		
### 2번. available_zones 함수

def available_zones():
	response = client.describe_availability_zones()
	for zone in response['AvailabilityZones']:
		print("[id] " + zone['ZoneId'], "[region] " + zone['RegionName'], "[zone] " + zone['ZoneName'])
			
	
###3번. start_instance 함수

def start_instance():
	id = input("Enter instance id: ")
	response = client.start_instances(InstanceIds=[id])
	print("Starting .... " + response['StartingInstances'][0]['InstanceId'])		
	if response['StartingInstances'][0]['CurrentState']['Name'] == 'pending':
		print("Successfully started instance " + response['StartingInstances'][0]['InstanceId'])
	else:
		print("Failed")

###5번. stop_instance 함수
def stop_instance():
	id = input("Enter instance id: ")
	response = client.stop_instances(InstanceIds=[id])	
	if response['StoppingInstances'][0]['CurrentState']['Name'] == 'stopping':
		print("Successfully stop instance " + response['StoppingInstances'][0]['InstanceId'])
	else:
		print("Failed")

### 메인 함수###
if __name__ == '__main__':
	number = 0
	while True:
		print("                                                            ")
		print("                                                            ")
		print("------------------------------------------------------------")
		print("           Amazon AWS Control Panel using SDK               ")
		print("                                                            ")
		print("  Cloud Computing, Computer Science Department              ")
		print("                           at Chungbuk National University  ")
		print("------------------------------------------------------------")
		print("  1. list instance                2. available zones        ")
		print("  3. start instance               4. available regions      ")
		print("  5. stop instance                6. create instance        ")
		print("  7. reboot instance              8. list images            ")
		print("                                 99. quit                   ")
		print("------------------------------------------------------------")
		number = int(input("Enter an integer:"))
		
		if number == 1:
			list_instance()
			
		elif number == 2:
			available_zones()
			
		elif number == 3:
			start_instance()
			
		elif number == 4:
			available_regions()
		
		elif number == 5:
			stop_instance()
			
		elif number == 4:
			reboot_instance()
		
