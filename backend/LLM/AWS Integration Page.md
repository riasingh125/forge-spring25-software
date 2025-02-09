TODO: 

Set up Amazon S3 service, can use independently of MongoDB, just need pandas to turn that health data into csv (light).

Set up Kendra- have it point to S3 bucket. Index our data in something like this for Python. 
"
import boto3
from botocore.exceptions import ClientError
import pprint
import time

kendra = boto3.client("kendra")

print("Create an index.")

# Provide a name for the index
index_name = "index-name"
# Provide an optional description for the index
description = "index description"
# Provide the IAM role ARN required for indexes
role_arn = "arn:aws:iam::${account id}:role/${role name}"

try:
    index_response = kendra.create_index(
        Name = index_name,
        Description = description,
        RoleArn = role_arn
    )

    pprint.pprint(index_response)

    index_id = index_response["Id"]

    print("Wait for Amazon Kendra to create the index.")

    while True:
        # Get the details of the index, such as the status
        index_description = kendra.describe_index(
            Id = index_id
        )
        # If status is not CREATING, then quit
        status = index_description["Status"]
        print(" Creating index. Status: "+status)
        if status != "CREATING":
            break
        time.sleep(60)

except  ClientError as e:
        print("%s" % e)

print("Program ends.")
"
This was off of Amazon, but describes general way indexes are created. After indexes are created though, 
we can create custom fields for our data mapping the indexes to and let Kendra filter the search results for what we need. 
With this, we can use the data to contact openAI API, train the model using chatGPT, so it knows what it'll be doing. We can just
prompt it with our trained dataset, giving it examples using our current dataset. 

Everytime a user inputs a new document, use Kendra to determine whether S3 already stores it. If not, parse the data using Python NLP libraries such as NLTK or Regex. We can then add the parsed data (likely in csv format) to S3.

For S3, import our CSV files, connect it to Kendra and set up the parameters. 

That means, for kkendra, use boto3 API in python. Kendra makes calls from the S3 storage, and with its query results, you can use Bedrock to generate LLM results. I think Kendra should also output the query results for the recommendation algorithm. 

For the recommendation algorithm, I'm looking into applying sckit-learn in order to normalize the data. Currently determining how to get numerical data from our queries. Will likely use fuzzy string matching with the user's data in order to get similarity scores, which lets us categorize numerical data. There are several methods for this, but I'm most familiar with Tf-idf (NLTK and SKlearn) and Levenshtein distance (FuzzyWuzzy in Python)

For Bedrock, can use Anthropic or Llama. If we're set on OpenAI, we might have to use AWS Lambda which enables us to make serverless calls to it. 

So final schema for project is User Call -> Kendra-> Reader Script -> S3 -> Kendra -> Recommendation -> User Call -> Bedrock -> User.