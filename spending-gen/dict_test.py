import csv
# from datetime import *
#import dateutil.tz
# from dateutil import tzlocal
import datetime

# from datetime import *
# from dateutil.tz import *

bucket_list = {'ResponseMetadata': {'RequestId': '0659128AED5C3A0B', 'HostId': 'ipTd957YNYk0EBY7QBe4iMJ0XwcQfH8jf5Vr1P4/3l6zx8pFEYE0ifG1mzxtD242aTdTVhh0PuM=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'ipTd957YNYk0EBY7QBe4iMJ0XwcQfH8jf5Vr1P4/3l6zx8pFEYE0ifG1mzxtD242aTdTVhh0PuM=', 'x-amz-request-id': '0659128AED5C3A0B', 'date': 'Thu, 29 Mar 2018 18:15:46 GMT', 'x-amz-bucket-region': 'eu-west-2', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'IsTruncated': False, 'Marker': 'public/oliverdhayden/', 'Contents': [{'Key': 'public/oliverdhayden/ML_CSV.csv', 'LastModified': "datetime.datetime(2018, 3, 29, 16, 1, 21, tzinfo=tzlocal())", 'ETag': '"c08b1b379c544cf63a0e79e770412385"', 'Size': 16887, 'StorageClass': 'STANDARD', 'Owner': {'ID': '46e8c6fda56fbc9ee8a33fc25c4d03431a7bcf5ab2cba33975b1ed708a5524d7'}}, {'Key': 'public/oliverdhayden/newest_statement.csv', 'LastModified': "datetime.datetime(2018, 3, 29, 16, 1, 21, tzinfo=tzlocal())", 'ETag': '"25de313dc803f7c6f35b93eb42ed0857"', 'Size': 285049, 'StorageClass': 'STANDARD', 'Owner': {'ID': '46e8c6fda56fbc9ee8a33fc25c4d03431a7bcf5ab2cba33975b1ed708a5524d7'}}, {'Key': 'uploads/README.txt', 'LastModified': "datetime.datetime(2018, 2, 27, 10, 19, 12, tzinfo=tzlocal())", 'ETag': '"81d1a0e5473f0188d4746070a186d3d9"', 'Size': 96, 'StorageClass': 'STANDARD', 'Owner': {'ID': '46e8c6fda56fbc9ee8a33fc25c4d03431a7bcf5ab2cba33975b1ed708a5524d7'}}], 'Name': 'pierandroid-userfiles-mobilehub-318679301', 'Prefix': '', 'MaxKeys': 1000, 'EncodingType': 'url'}

print(bucket_list["Contents"])
print("---------------")
test = bucket_list["Contents"]
for i in test:
    print(i)
    print("-----------")
