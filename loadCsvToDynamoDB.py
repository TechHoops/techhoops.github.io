import boto3
import pandas as pd
import json
import argparse, sys
import os

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("--dataFile", help="Please provide the csv file name to load the data from")
    parser.add_argument("--tableName", help="Please provide the table name to load data in to")
    parser.add_argument("--profile", help="Provide aws profile name if not provided default will be used", default='default')
    parser.add_argument("--verbose", help="Verbose operation", default=False)

    args=parser.parse_args()

    tableName = args.tableName
    dataFile = args.dataFile
    awsProfile = args.profile
    verbosity = args.verbose

    if tableName == None and dataFile == None:
        print("tableName and dataFile are required arguments, -h for help")
        sys.exit()

    #Connect to DynamoDb Function
    session = boto3.Session(profile_name=awsProfile)
    dynamodb = session.client('dynamodb')

    if os.path.isfile(args.dataFile) == False:
        sys.exit()
    
    print("Input file exists!")

    table_validation_response = dynamodb.describe_table(TableName=tableName)
    if table_validation_response:
        ## parse csv data
        tableData_json = json.loads(pd.read_csv(dataFile).to_json(orient="records"))
        insertDynamoItem(awsProfile,verbosity,tableName,tableData_json)
        print("Table found!")

def insertDynamoItem (awsProfile,verbosity, tablename,item_lst):
    session = boto3.Session(profile_name=awsProfile)
    dynamodbResourceClient = session.resource('dynamodb')
    dynamoTable = dynamodbResourceClient.Table(tablename)

    for record in item_lst:
        if verbosity:
            print(record)
        dynamoTable.put_item(Item=record)

    print('Success')

if __name__ == "__main__":
    main()