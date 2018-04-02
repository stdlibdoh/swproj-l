import csv
import ntpath
from datetime import date
from datetime import timedelta
import os
import os.path
import boto3


s3_client = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    folder, fileName = ntpath.split(key)

    fileNameNoExten = fileName[0:len(fileName)-4]

    print(folder)
    print(fileName)
    print(fileNameNoExten)

    #put uploaded file into tmp folder
    temp_uploaded_csv_path = "/tmp/"+fileName
    s3_client.download_file(bucket, key, temp_uploaded_csv_path)

    #"public/"+fileNameNoExten+"/"
    bucket_list = s3_client.list_objects(Bucket = bucket, Marker = "public/")
    print(bucket_list)
    print(bucket_list['Contents'])

    global_statement_exists = False
    global_ml_exists = False


    #check if the files already exist in bucket
    for item in bucket_list['Contents']:
        print(item['Key'])
        #if the global bank statement csv exists download it to tmp
        if item['Key'] == 'public/'+fileNameNoExten+'/global_statement.csv':
            print("found a global statement")
            global_statement_exists = True
            s3_client.download_file(bucket, 'public/'+fileNameNoExten+'/global_statement.csv', '/tmp/global_statement.csv')
        #if the global ml csv exists download it to tmp
        if item['Key'] == 'public/'+fileNameNoExten+'/global_ml.csv':
            print("found a global ml file")
            global_ml_exists = True
            s3_client.download_file(bucket, 'public/'+fileNameNoExten+'/global_statement.csv', '/tmp/global_statement.csv')


    #create the global bank statement if it does not exist
    if global_statement_exists == False:
        print("global bank statement does not exist")
        with open('/tmp/global_statement.csv','w',newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['Day','Month','Year','Description', 'Category','Value','Balance']);

    #create the global ml csv if it does not exist
    if global_ml_exists == False:
        print("global ml csv does not exist")
        with open('/tmp/global_ml.csv','w',newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')

    #split out balances for ML in tmp folder
    #save the path to the var
    ML_CSV_path = extractBalance(temp_uploaded_csv_path)

    #concat the new ML to the global ML csv
    ML_concat("/tmp/global_ml.csv", ML_CSV_path)

    #concat the new bank statement with the gobal bank statement
    bank_statement_concat("/tmp/global_statement.csv", temp_uploaded_csv_path)

    #upload the concatinated global bank statement
    s3_client.upload_file("/tmp/global_statement.csv", bucket, "public/"+fileNameNoExten+"/global_statement.csv")

    #upload the concatinated global ml csv
    s3_client.upload_file("/tmp/global_ml.csv", bucket, "public/"+fileNameNoExten+"/global_ml.csv")



    #get global bank statement cvs from bucket
    #s3_client.download_file(bucket, "public/"+fileNameNoExten+"/global_statement.csv", "/tmp/global_statement.csv")

    #concat the new bank statement with the gobal bank statement
    #bank_statement_concat("/tmp/global_statement.csv", temp_uploaded_csv_path)

    #upload global csv back to bucket
    #s3_client.upload_file("/tmp/global_statement.csv", bucket, "public/"+fileNameNoExten+"/global_statement.csv")



    #s3_client.upload_file(temp_uploaded_csv_path, bucket, "public/"+fileNameNoExten+"/newest_statement.csv")


    #s3_client.upload_file(ML_CSV_path, bucket, "public/"+fileNameNoExten+"/ML_CSV.csv")

    # s3_client.upload_file("/tmp/ML_CSV.csv", bucket, folder+"/ML_CSV.csv")
    print("end of functions")
    return "hello"




    #s3_client.upload_file(download_path, bucket, folder+"/Ollie.csv")

def ML_concat(csv1, csv2):
    main = open(csv1,"a")
    for row in open(csv2):
        main.write(row)

def bank_statement_concat(csv1, csv2):
    main = open(csv1,"a")
    first_row = True
    for row in open(csv2):
        if first_row:
            first_row = False
        else:
            main.write(row)



def extractBalance(csv_path):
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile)
        with open("/tmp/ML_CSV.csv",'w',newline='') as ML_CSV:
            print("1")
            writer = csv.writer(ML_CSV, delimiter=',')

            # for row in reader:
            #     writer.writerow([row[-1]])


            firstLine = True
            current_date = date(2010,1,1)
            previous_date = date(2010,1,2)
            previous_row = None

            counter = 0
            for row in reader:
                if firstLine:
                    firstLine = False
                else:
                    current_date = date(int(row[2]),int(row[1]),int(row[0]))
                    if current_date != previous_date:
                        difference_in_dates = current_date-previous_date
                        difference_in_days = timedelta(difference_in_dates.days)
                        for i in range(0,difference_in_days.days-1):
                            writer.writerow([previous_row])


                        previous_date = date(int(row[2]),int(row[1]),int(row[0]))
                        previous_row = row[-1]
                        writer.writerow([row[-1]])
    return "/tmp/ML_CSV.csv"
