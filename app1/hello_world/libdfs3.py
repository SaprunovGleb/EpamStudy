import pandas as pd
import boto3 
import io
def read_csv_from_s3(Bucket, csvname):
    s3 = boto3.resource('s3')    
    bucket_names = []
    key_names = []
    for bucket in s3.buckets.all():
        bucket_names.append(bucket.name)
    bucket = s3.Bucket(Bucket)
    for key in bucket.objects.all():
        key_names.append(key)
    get_object_response = s3.Object(Bucket,csvname)
    #print(get_object_response.get())
    file = get_object_response.get()['Body']
    df = pd.read_csv(file, sep=',')
    return df

def filter_df(df, column, key):
    df2 = df[df[column] == key]
    return df2

def write_df_to_s3(df, Bucket, csvname):
    s3 = boto3.resource('s3') 
    bucket = s3.Bucket(Bucket)
    s_buf = io.StringIO()
    #print(df)
    df.to_csv(s_buf,index=False)
    s_buf.seek(0)
    #print("no read",s_buf)
    #print("read",s_buf.read())
    bucket.put_object(ACL='bucket-owner-full-control',Body=s_buf.read(), ContentEncoding="UTF-8", Key = csvname)
    return True

def write_df_to_db(df, DataBaseName, DataBaseArn):
    client = boto3.client('rds')
    return False
                       