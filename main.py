import boto3
import os.path

class Amazon:
     
    def __init__(self,filename,aws_access_key_id,aws_secret_access_key,region_name,source_bucket,destination_bucket):
        
        self.filename = filename
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self.source_bucket = source_bucket
        self.destination_bucket = destination_bucket
  
    def create_file(self):
    
    	if os.path.exists(str(os.getcwd() + '/' + self.filename)):
    		return self.filename
    	else:
    		with open(self.filename, 'wb') as data:
    			data.seek(5368709120 - 1)
    			data.write(bytes("\0", 'UTF-8'))
    		return data
    		
    	
    def upload_file(self):

    	session = boto3.Session(
        	aws_access_key_id=self.aws_access_key_id,
        	aws_secret_access_key=self.aws_secret_access_key,
        	region_name=self.region_name
    	)

    	s3 = session.resource('s3')
    	bucket = s3.Bucket('YOUR_BUCKET_NAME')
    	data = open(self.filename, 'rb')
    	s3.Bucket('YOUR_BUCKET_NAME').put_object(Key=data.name, Body=data)

    def getFilename(self):

    	#file = open(self.filename)
    	return os.path.basename(open(self.filename).name)

    def copy_file(self):

    	s3 = boto3.client('s3',aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    	copy_source = {'Bucket': self.source_bucket,'Key': self.getFilename}
    	s3.copy_object(CopySource=copy_source,Bucket=self.destination_bucket,Key=self.getFilename())

if __name__ == "__main__":

    key_id = 'YOUR_AWS_ACESS_KEY_ID'
    access_key = 'YOUR_AWS_SECRET_ACCESS_KEY_ID'
    region_name = 'YOUR_AWS_ACCOUNT_REGION'
    file = 'my_file'
    source_bucket = 'source_bucket'
    destination_bucket = 'destination_bucket'
    
    aws = Amazon(file,key_id,access_key,region_name,source_bucket,destination_bucket)
    aws.create_file()
    aws.upload_file()
    aws.copy_file()
