import json
import pandas as pd
import libdfs3
def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    df = pd.DataFrame([[1,2,3],[4,5,6]], columns=['1','2', '3'])
    df = libdfs3.read_csv_from_s3("lambdabucketsaprunovglebinput", "airportspart.csv")
    df = libdfs3.filter_df(df, "type", "heliport")
    libdfs3.write_df_to_s3(df,"lambdabucketsaprunovglebresult","airportsfiltered.csv")
    #print(df)
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "csv filtered and saved",
            }
        )
    }