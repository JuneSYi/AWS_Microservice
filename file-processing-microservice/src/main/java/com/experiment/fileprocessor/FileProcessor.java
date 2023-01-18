package com.experiment.fileprocessor;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.List;

import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.PutObjectRequest;
import com.amazonaws.services.s3.model.S3Object;
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
import com.amazonaws.services.sqs.model.Message;
import com.amazonaws.services.sqs.model.ReceiveMessageRequest;

public class FileProcessor {

	private static AmazonS3 s3Client = AmazonS3ClientBuilder.defaultClient();
	private static AmazonSQS sqsClient = AmazonSQSClientBuilder.defaultClient();
	
	/**
	 * a method that will poll the SQS queue for new messages. Once a new message is received, 
	 * it should parse the message to get the S3 key for the file to be processed, download the 
	 * file from S3, perform the processing, and then upload the processed file back to S3.
	 */
	public void processFiles(){
	    //Poll SQS Queue
	    String queueUrl = "https://sqs.us-west-2.amazonaws.com/account-id/queue-name";
	    ReceiveMessageRequest receiveMessageRequest = new ReceiveMessageRequest(queueUrl);
	    List<Message> messages = sqsClient.receiveMessage(receiveMessageRequest).getMessages();
	    
	    for(Message message : messages){
	        //Parse S3 key
	        String s3Key = message.getBody();
	        //Download file from S3
	        S3Object s3Object = s3Client.getObject(new GetObjectRequest("bucket-name", s3Key));
	        //Perform processing
	        File processedFile = performProcessing(s3Object.getObjectContent());
	        //Upload processed file to S3
	        s3Client.putObject(new PutObjectRequest("bucket-name", "processed/"+s3Key, processedFile));
	    }
	}
	
	// if text file
	private File performProcessing(InputStream inputStream) {
	    BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
	    // create a new File object to hold the processed file
	    File processedFile = new File("path/to/processedFile.txt");
	    try (BufferedWriter writer = new BufferedWriter(new FileWriter(processedFile))) {
	        String line;
	        while ((line = reader.readLine()) != null) {
	            // perform some operations on the line
	            // for example, replace all occurrences of "oldWord" with "newWord"
	            line = line.replaceAll("oldWord", "newWord");
	            // write the processed line to the processed file
	            writer.write(line);
	            writer.newLine();
	        }
	    } catch (IOException e) {
	        e.printStackTrace();
	    }
	    return processedFile;
	}
}
