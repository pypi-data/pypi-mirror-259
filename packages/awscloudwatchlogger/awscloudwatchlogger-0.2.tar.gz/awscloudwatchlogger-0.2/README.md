# python setup.py sdist bdist_wheel
# twine upload dist/*
from awslogger import CloudWatchLogger
import logging

# Replace 'your_aws_key' and 'your_aws_secret' with actual values
# Create an instance of the CloudWatchLogger class
logger = CloudWatchLogger(ACCESS_KEY, SECRET_KEY, REGION_NAME)
logger.set_log_level(logging.ERROR)  # Set logging level to INFO

log_group_name = 'my-log-group'
log_stream_name = 'my-log-stream'
logger.create_log_group(log_group_name)
logger.create_log_stream(log_group_name, log_stream_name)


function_name = 'Test function'

# # Log at different levels
logger.put_log_event(log_group_name, log_stream_name, "This is info message.", function_name, log_level=logging.INFO)
logger.put_log_event(log_group_name, log_stream_name, "This is debug message.", function_name, log_level=logging.DEBUG)
logger.put_log_event(log_group_name, log_stream_name, "This is warning message.", function_name, log_level=logging.WARNING)
logger.put_log_event(log_group_name, log_stream_name, "This is critical message.", function_name, log_level=logging.CRITICAL)
logger.put_log_event(log_group_name, log_stream_name, "This is error message.", function_name, log_level=logging.ERROR)

