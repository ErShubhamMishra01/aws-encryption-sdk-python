KMS Tutorial and reference blogs:-
----------------------------------
https://www.youtube.com/watch?v=f3APF1dP8w0

https://enlear.academy/data-encryption-on-aws-8d6be6033351

https://enlear.academy/data-encryption-on-aws-part-02-ecb5b1e15451

https://enlear.academy/aws-encryption-sdk-d38bfae40e9f


docker run --rm -ti -v ~/.aws:/root/.aws amazon/aws-cli kms generate-data-key --key-id alias/test-kms --key-spec AES_256 --region eu-central-1

echo ""| base64 --decode > ~/.aws/kms/ctk

echo "AQIDAHhMb3xeU2yCGxfBfuJPfcKfPvgHQjUNDkdwI8ZoFSXRqgGcdBYtZtmQIq/64TgKLhR2AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMjSFuHe9V331ZoRcyAgEQgDvzWvoJBEum9Dufpr5p9yggjqM9Q43ZfuVD5P8DXU6/gtxEeT0hM0jMwtrS+eWoMX44GoVnyAu7bL4Szw=="| base64 --decode > ~/.aws/kms/ctk

echo "ogZ8DDbjEpmRIneCybaeFFwUuuUzbYQAf0DrD0lpEKI="| base64 --decode > ~/.aws/kms/ptk

echo this is plain text > ~/.aws/kms/mydata.txt

openssl enc -in .aws/kms/mydata.txt -out .aws/kms/mydata-encrypted.txt -e -aes256 -k .aws/kms/ptk

docker run --rm -ti -v ~/.aws:/root/.aws amazon/aws-cli kms decrypt --ciphertext-blob fileb:///root/.aws/kms/ctk  --region eu-central-1

openssl enc -in .aws/kms/mydata-encrypted.txt -out .aws/kms/mydata-decrypted.txt -d -aes256 -k .aws/kms/ptk
