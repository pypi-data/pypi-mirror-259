from awskit.interface import AwsInterface


class Sqs(AwsInterface):

    def __init__(self):
        super().__init__("sqs", "2012-11-05")

    def CreateQueue(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, creates a queue

        QueueName
        """

        resp = self.post(region, "CreateQueue", **kwargs)
        return resp["CreateQueueResponse"]

    def ListQueues(self, region: str) -> list:
        """
        Given a region, returns a list of all queues available in that region
        """

        resp = self.get(region, "ListQueues")
        return resp["ListQueuesResponse"]

    def DeleteQueue(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, deletes a queue

        QueueUrl
        """

        resp = self.post(region, "DeleteQueue", **kwargs)
        return resp["DeleteQueueResponse"]

    def SendMessage(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, sends a message
        """

        resp = self.post(region, "SendMessage", **kwargs)
        return resp["SendMessageResponse"]
    
    def ReceiveMessage(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, receives a message
        """

        resp = self.post(region, "ReceiveMessage", **kwargs)
        return resp["ReceiveMessageResponse"]

    def DeleteMessage(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, deletes a message
        """

        resp = self.post(region, "DeleteMessage", **kwargs)
        return resp["DeleteMessageResponse"]
