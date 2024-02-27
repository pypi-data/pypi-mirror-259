import logging
import boto3
from botocore.exceptions import ClientError
import time
import uuid

class CloudWatchLogger:
    def __init__(self, aws_key, aws_secret, region_name, log_level=logging.INFO):
        self.aws_key = aws_key
        self.aws_secret = aws_secret
        self.region_name = region_name
        self.logs_client = self._get_cloudwatch_logs_client()
        self.log_level = log_level

    def _get_session(self):
        session = boto3.Session(
            aws_access_key_id=self.aws_key,
            aws_secret_access_key=self.aws_secret,
            region_name=self.region_name
        )
        return session

    def _get_cloudwatch_logs_client(self):
        session = self._get_session()
        return session.client('logs')

    def create_log_group(self, log_group_name):
        try:
            self.logs_client.create_log_group(logGroupName=log_group_name)
            logging.info(f"Log group '{log_group_name}' created successfully.")
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceAlreadyExistsException':
                logging.info(f"Log group '{log_group_name}' already exists.")
            else:
                logging.error(f"Failed to create log group '{log_group_name}': {e}")

    def create_log_stream(self, log_group_name, log_stream_name):
        try:
            self.logs_client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
            logging.info(f"Log stream '{log_stream_name}' created successfully.")
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceAlreadyExistsException':
                logging.info(f"Log stream '{log_stream_name}' already exists.")
            else:
                logging.error(f"Failed to create log stream '{log_stream_name}': {e}")

    def put_log_event(self, log_group_name, log_stream_name, message, function_name, log_level=logging.INFO):
        session_id = str(uuid.uuid4())
        try:
            if log_level >= self.log_level:  # Check if provided log level is sufficient
                response = self.logs_client.put_log_events(
                    logGroupName=log_group_name,
                    logStreamName=log_stream_name,
                    logEvents=[
                        {
                            'timestamp': int(time.time() * 1000),
                            'message': f"\nMessage: {message}\nFunction: {function_name}\nSession ID: {session_id}"
                        }
                    ]
                )
                if log_level >= logging.INFO:
                    logging.info(response)
                elif log_level >= logging.DEBUG:
                    logging.debug(response)
                elif log_level >= logging.WARNING:
                    logging.warning(response)
                elif log_level >= logging.ERROR:
                    logging.error(response)
                elif log_level >= logging.CRITICAL:
                    logging.critical(response)
        except ClientError as e:
            logging.error(f"Failed to put log event: {e}")

    def set_log_level(self, log_level):
        self.log_level = log_level
