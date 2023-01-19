package com.experiment.fileprocessor;
import java.util.List;

import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
import com.amazonaws.services.sqs.model.Message;
import com.amazonaws.services.sqs.model.ReceiveMessageRequest;

public class FileProcessor {

	//Credentials
	private static BasicAWSCredentials user = new BasicAWSCredentials("ACCESS_KEY","SECRET_KEY");
	// creating an instance of S3
	private static AmazonS3 s3Instance = AmazonS3ClientBuilder.standard()
			.withCredentials(new AWSStaticCredentialsProvider(user))
			.build();
	// creating an instance of Amazon SQS - https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/sqs/AmazonSQSClientBuilder.html
	private static AmazonSQS sqsInstance = AmazonSQSClientBuilder.standard()
			.withCredentials(new AWSStaticCredentialsProvider(user))
			.build();

	// polling the SQS queue for new messages
	public void pollMessages() {
		// Set destination path
		String sqsURL = "https://CREATE_SQS_INPUT_URL";
		// receive the messages
		ReceiveMessageRequest rmr = new ReceiveMessageRequest(sqsURL);
		// getMessages() returns the list of messages received
		// receiveMessage() is an instance of ReceiveMessageResult class which access messages,
		// receipts handles, and other metadata
		List<Message> messages = sqsInstance.receiveMessage(rmr).getMessages();
		
		for (Message message : messages) {
			// get message content
			String content = message.getBody();
			// every object within s3 has an Amazon S3 key which we'll need to parse
			S3Object object =
					
			// process the file and delete if it contains marked words
					
			// upload the file back
					
		}
	}
	
	// function for file processing
}

// SQS builder: https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsClientBuilder.html
// SQS doc: https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsClient.html
// Apache Commons IO for working with files and input/output streams
// Apache Tika for text files parsing