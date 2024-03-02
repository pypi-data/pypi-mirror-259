"""
Testing Strategy

create two queue
- 1 fifo queue
- 1 standard queue

create two topic
- 1 fifo topic
- 1 standard topic

subscribe the fifo queue to both the fifo topic and the standard topic
subscribe the standard queue to both the fifo topic and the standard topic
"""

# Run the following commands to test the above strategy
# python manage.py shell

from pubsublib.aws.main import AWSPubSubAdapter
pubsub_adapter = AWSPubSubAdapter(
  aws_region='ap-south-1',
  aws_access_key_id='AKIAY2NYR4DWCDQEIVNO',
  aws_secret_access_key='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',
  redis_location='redis://redis.staging.svc.cluster.local:6379/190'
)

topic_1 = pubsub_adapter.create_topic(
    topic_name='testing_pubsublib_fifo_topic_1.fifo',
    is_fifo=True,
    tags={
        "environment": "dev",
        "service_name": "pubsublib",
        "contains_sensitive_data": "true",
        "city_code": "ALL"
    },
)
print(topic_1)
"""
{'TopicArn': 'arn:aws:sns:ap-south-1:606514307308:testing_pubsublib_fifo_topic_1.fifo', 'ResponseMetadata': {'RequestId': '630b46a1-79e3-58ff-8f9f-18fac0ee4a3a', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '630b46a1-79e3-58ff-8f9f-18fac0ee4a3a', 'date': 'Fri, 01 Mar 2024 11:06:53 GMT', 'content-type': 'text/xml', 'content-length': '343', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
"""

topic_2 = pubsub_adapter.create_topic(
    topic_name='testing_pubsublib_standard_topic_1',
    is_fifo=False,
    tags={
        "environment": "dev",
        "service_name": "pubsublib",
        "contains_sensitive_data": "true",
        "city_code": "ALL"
    },
)
print(topic_2)
"""
{'TopicArn': 'arn:aws:sns:ap-south-1:606514307308:testing_pubsublib_standard_topic_1', 'ResponseMetadata': {'RequestId': '87d2d734-b934-5788-bc65-896f005434a9', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '87d2d734-b934-5788-bc65-896f005434a9', 'date': 'Fri, 01 Mar 2024 11:08:16 GMT', 'content-type': 'text/xml', 'content-length': '342', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
"""

queue_1 = pubsub_adapter.create_queue(
    name='testing_pubsublib_fifo_queue_1.fifo',
    is_fifo=True,
    tags={
        "environment": "dev",
        "service_name": "pubsublib",
        "contains_sensitive_data": "true",
        "city_code": "ALL"
    },
)
print(queue_1)
"""
{'QueueUrl': 'https://sqs.ap-south-1.amazonaws.com/606514307308/testing_pubsublib_fifo_queue_1.fifo', 'ResponseMetadata': {'RequestId': 'f3e3e3e3-3e3e-3e3e-3e3e-3e3e3e3e3e3e', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'f3e3e3e3-3e3e-3e3e-3e3e-3e3e3e3e3e3e', 'date': 'Fri, 01 Mar 2024 11:09:47 GMT', 'content-type': 'text/xml', 'content-length': '319', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
"""

queue_2 = pubsub_adapter.create_queue(
    name='testing_pubsublib_standard_queue_1',
    is_fifo=False,
    visiblity_timeout = "30",
    message_retention_period = "345600", #4days
    content_based_deduplication = "true",
    tags={
        "environment": "dev",
        "service_name": "pubsublib",
        "contains_sensitive_data": "true",
        "city_code": "ALL"
    },
)
print(queue_2)


subscribe_details = pubsub_adapter.subscribe_to_topic(
    sns_topic_arn = 'arn:aws:sns:ap-south-1:606514307308:testing_pubsublib_fifo_topic_1.fifo',
    sqs_queue_arn= 'https://sqs.ap-south-1.amazonaws.com/606514307308/testing_pubsublib_fifo_queue_1.fifo',
    raw_message_delivery= False,
    filter_policy = "a"
)
print(subscribe_details)