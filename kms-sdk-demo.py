import aws_encryption_sdk
from aws_encryption_sdk import CommitmentPolicy
import sys
import traceback

def cycle_string(key_arn, source_plaintext, botocore_session=None):
    """Encrypts and then decrypts a string under an &KMS; key.

    :param str key_arn: Amazon Resource Name (ARN) of the &KMS; key
    :param bytes source_plaintext: Data to encrypt
    :param botocore_session: existing botocore session instance
    :type botocore_session: botocore.session.Session
    """
    # Set up an encryption client with an explicit commitment policy. If you do not explicitly choose a
    # commitment policy, REQUIRE_ENCRYPT_REQUIRE_DECRYPT is used by default.
    client = aws_encryption_sdk.EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT)

    # Create an AWS KMS master key provider
    kms_kwargs = dict(key_ids=[key_arn])
    if botocore_session is not None:
        kms_kwargs["botocore_session"] = botocore_session
    master_key_provider = aws_encryption_sdk.StrictAwsKmsMasterKeyProvider(**kms_kwargs)

    # Encrypt the plaintext source data
    ciphertext, encryptor_header = client.encrypt(source=source_plaintext, key_provider=master_key_provider)
    print("Cipher Text")
    print(ciphertext)
    # Decrypt the ciphertext
    cycled_plaintext, decrypted_header = client.decrypt(source=ciphertext, key_provider=master_key_provider)
    cycled_plaintext=cycled_plaintext.decode("utf-8")
    print("Cycled Text (Plain Text)")
    print(cycled_plaintext)
    assert cycled_plaintext == source_plaintext
    
    assert all(
        pair in decrypted_header.encryption_context.items() for pair in encryptor_header.encryption_context.items()
    )

plain_text="This is sample plain text, it can contain sensitive information."
print("Plain Text")
print(plain_text)
cycle_string("arn:aws:kms:eu-central-1:564119825769:key/32d5d7e7-7251-4dec-bbc3-97333a20ce88",plain_text)
print("END")