# Experimenting with Lambda
#
### Objective
- File processing service that uses S3, SQS, and Lambda
- Code will run in Lambda function every X minutes to poll the SQS queue for new messages, download the corresponding files from s3, 
remove all files that contain the following classified key words "hydra" "Ten rings" "deadpool", and return the other files back to the s3 bucket

### Plan
- Use Maven to build a quickstart project
- Add AWS SDK dependency to communicate with AWS services
- Create IAM role, S3 bucket, SQS
- Write the code to communicate with SQS and S3
- package into a JAR file using mvn package clean
- Create a lambda function and incorporate JAR file (tie it to cloudwatch events to make it persistent/periodic)
- test
- fail the test
- redo the code
- test again
- spend 20 hours debugging and eventually figure it out

### Process
1. Maven CLI: mvn archetype:generate -DgroupId=com.experiment -DartifactId=file-processing-microservice -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
2. Added AWS SDK to pom.xml
3. Created FileProcessor.java file
4. Added Apache Maven Shade Plugin to pom.xml
	- to package your JAR file with the artifacts in an uber JAR, which consists of all dependencies required to run the project.

#### For my own personal education:
More on S3, sqs, lambda
- https://aws.plainenglish.io/system-design-s3-events-to-lambda-vs-s3-events-to-sqs-sns-to-lambda-2d41477d1cc9
creating scheduled events to invoke lambda functions
- https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_scheduled_events
Primary site for documentation
- https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/overview-summary.html


