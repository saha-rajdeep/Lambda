//Make this Lambda function triggered by the S3 bucket object add for the AWS
//CodeBuild Output
console.log('Loading function');
var AWS = require('aws-sdk');
var lambda = new AWS.Lambda();
exports.handler = function(event, context) {
    key = event.Records[0].s3.object.key
    bucket = event.Records[0].s3.bucket.name
    version = event.Records[0].s3.object.versionId
    if (bucket == "lambda-package-deploy01" && key == "codedeployoutput.zip" && version) {
        var functionName = "codedeployoutput";
        console.log("uploaded to lambda function: " + functionName);
        var params = {
            Code:{
            S3Key: key,
            S3Bucket: bucket,
            S3ObjectVersion: version
            },
            FunctionName: functionName,
            Role: "arn:aws:iam::lambda_role", // replace with the actual arn of the execution role you created
            Runtime: "python2.7", //Runtime environment of the application lambda
            Handler: "lambda_handler"
        };
        lambda.createFunction(params, function(err, data) {
            if (err) {
                console.log(err, err.stack);
                context.fail(err);
            } else {
                console.log(data);
                context.succeed(data);
            }
        });
    } else {
        context.succeed("skipping zip " + key + " in bucket " + bucket + " with version " + version);
    }
};