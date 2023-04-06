# aws-encryption-sdk-python
Goal: show how to do asymmetric encryption and decryption with Aws Kms in Python.

Steps:
1. Create an Iam user with programmatic access
2. Review attached policies to this user
3. Copy the access key and secret access key and congigure it on aws cli
4. Go to the KMS page in the console - create a key (Choose: Asymmetric)
Note that the key spec you choose will require specific EncryptionAlgorithm choices
5. Choose the Iam user you just made as a key admin
6. Choose the Iam user you just made as a key user
7. Click finish
8. Make sure you made your Iam User + Kms key in the correct region for the boto3 Kms client.
9. use the ARN (key_arn) of the Kms key that you just made: Example- arn:aws:kms:us-east-2:847689995987:key/e13e3762-04c4-4fba-a57f-4c93beb4e935
