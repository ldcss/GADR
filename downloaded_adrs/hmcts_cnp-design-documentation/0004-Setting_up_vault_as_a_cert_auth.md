# 4. Setting up Vault as a Certification Authority (CA)
Date: 2017-07-27

## Status 
Accepted

## Context 

We wanted to explore Vault's capabilities to serve as a CA for services deployed on the strategic platform at HMCTS, that's to issue the certificates services may need for authentication purposes. 

## Decision 

In order to discuss the CA capabilities Vault has we need first to talk about Secret Backends. Secret Backends are the components in Vault which store and generate secrets, they are part of the mount system in Vault. They behave very similarly to a virtual filesystem: any read/write/delete is sent to the secret backend, and the secret backend can choose to react to that operation however it sees fit.

For CA purposes Vault provides the PKI Secret Backend which generates X.509 certificates dynamically based on configured roles. This means services can get certificates needed for both client and server authentication without going through the usual manual process of generating a private key and CSR, submitting to a CA, and waiting for a verification and signing process to complete.

Vault's documentation [quick-start](https://www.vaultproject.io/docs/secrets/pki/index.html#quick-start) on this subject illustrate pretty well some of the operational concepts behind running Vault as a CA. The documentation also presents some of the [considerations](https://www.vaultproject.io/docs/secrets/pki/index.html#considerations) needed when using the PKI backend but we believe the ["Be Careful with Root CAs"](https://www.vaultproject.io/docs/secrets/pki/index.html#be-careful-with-root-cas) section require special attention and that's why we focused our spike on showing how Vault can be used to create a Root CA and an Intermediate CA for our organization.

With the above in mind we start by creating the Root CA for our org. We begin by mounting the PKI backend for our hmcts Root CA:

```code
/ # vault mount -path=hmcts -description="HMCTS Root CA" pki
Successfully mounted 'pki' at 'hmcts'!
/ #
```

Now we can create the CA certificate

```code
/ # vault write hmcts/root/generate/internal \
> common_name="HMCTS Root CA" \
> key_bits=4096 \
> exclude_cn_from_sans=true
Key             Value
---             -----
certificate     -----BEGIN CERTIFICATE-----
MIIFADCCAuigAwIBAgIUd0VBVb7dPA3fO8X36dt9LVhBpVcwDQYJKoZIhvcNAQEL
BQAwGDEWMBQGA1UEAxMNSE1DVFMgUm9vdCBDQTAeFw0xNzA3MjcxNTU3MzRaFw0x
NzA4MjgxNTU4MDRaMBgxFjAUBgNVBAMTDUhNQ1RTIFJvb3QgQ0EwggIiMA0GCSqG
...
<output truncated>
...
-----END CERTIFICATE-----
expiration      1503935884
issuing_ca      -----BEGIN CERTIFICATE-----
MIIFADCCAuigAwIBAgIUd0VBVb7dPA3fO8X36dt9LVhBpVcwDQYJKoZIhvcNAQEL
BQAwGDEWMBQGA1UEAxMNSE1DVFMgUm9vdCBDQTAeFw0xNzA3MjcxNTU3MzRaFw0x
NzA4MjgxNTU4MDRaMBgxFjAUBgNVBAMTDUhNQ1RTIFJvb3QgQ0EwggIiMA0GCSqG
...
<output truncated>
...
4QnBYzvMNlxCHyhlrmG7+TzRXRYEV2HSV9VNX0/+DfGxo2Xk2UsXYDq3BvwUPkk7
W47N/TSaO1kFNMFhE+QNeAzddp4SFrpoWrIZ1Z1mPo12Jl8aW89hzbj8CUHtv12t
6/U0lfBERcz13VzPl5pAfEWQs3/DJcfKJXVodkcMaD7BhDkk
-----END CERTIFICATE-----
serial_number   77:45:41:55:be:dd:3c:0d:df:3b:c5:f7:e9:db:7d:2d:58:41:a5:57

/ #
```

Using `curl` and `openssl` we can verify the certificate we just created:

```code
/ # curl -s http://127.0.0.1:1234/v1/hmcts/ca/pem | openssl x509 -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            77:45:41:55:be:dd:3c:0d:df:3b:c5:f7:e9:db:7d:2d:58:41:a5:57
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=HMCTS Root CA
        Validity
            Not Before: Jul 27 15:57:34 2017 GMT
            Not After : Aug 28 15:58:04 2017 GMT
        Subject: CN=HMCTS Root CA
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
                Modulus:
                    00:a1:d8:f3:2a:43:09:6c:39:42:4e:f1:b8:c9:86:
                    82:e5:ed:4e:34:b2:92:f7:c6:d2:68:10:a2:46:ec:
...
<output truncated>
```

We can now proceed to configure the URL's for accessing not only the CA but also the Certificate Revocation List (CRL):

```code
/ # vault write hmcts/config/urls issuing_certificates="http://127.0.0.1:1234/v1/hmcts"
Success! Data written to: hmcts/config/urls
/ # 
```

Note that we used the localhost ip address in the issuing_certificates URL only for demo purposes and this can be set to any address as appropriate. With the Root CA ready we can now create an Intermediate CA:

```code
/ # vault write hmcts/config/urls issuing_certificates="http://127.0.0.1:1234/v1/hmcts"
Success! Data written to: hmcts/config/urls
/ # vault mount -path=hmcts_probate -description="Probate Intermediate CA" pki
Successfully mounted 'pki' at 'hmcts_probate'!
/ # vault mounts
Path            Type       Default TTL  Max TTL  Force No Cache  Replication Behavior  Description
cubbyhole/      cubbyhole  n/a          n/a      false           local                 per-token private secret storage
hmcts/          pki        system       system   false           replicated            HMCTS Root CA
hmcts_probate/  pki        system       system   false           replicated            Probate Intermediate CA
secret/         generic    system       system   false           replicated            generic secret storage
sys/            system     n/a          n/a      false           replicated            system endpoints used for control, policy and debugging
/ #
```
Now we proceed to generate the Intermediate Certificate Signing Request (CSR):

```code
 / # vault write hmcts_probate/intermediate/generate/internal \
> common_name="Probate Intermediate CA" \
> key_bits=4096 \
> exclude_cn_from_sans=true
Key     Value
---     -----
csr     -----BEGIN CERTIFICATE REQUEST-----
MIIEZzCCAk8CAQAwIjEgMB4GA1UEAxMXUHJvYmF0ZSBJbnRlcm1lZGlhdGUgQ0Ew
ggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDBAzV85KEbAH3UYgxrR6F5
...
<output truncated>
...
qoaquy/+vS6o5Fg2e4XE0ZNMDpTj37visONk
-----END CERTIFICATE REQUEST-----

/ #
```

Now we need to use the CSR to get a cert signed by the Root CA. For this we save/copy the contents of the CSR onto a file (`probate.csr`) and send it to the Root CA backend:

```code
/ # vault write hmcts/root/sign-intermediate \
> csr=@probate.csr \
> common_name="Probate Intermediate CA" \
> ttl=24h
Key             Value
---             -----
certificate     -----BEGIN CERTIFICATE-----
MIIFjTCCA3WgAwIBAgIUUGSq+TcwSQnLtkFP5WjS/yk1T5kwDQYJKoZIhvcNAQEL
BQAwGDEWMBQGA1UEAxMNSE1DVFMgUm9vdCBDQTAeFw0xNzA3MjcxNjMzMTNaFw0x
...
<output truncated>
...
IAO2K7gqK1gVV1DmXWSpmTcT4mUXFgGWtM3TP2ILV3lYRzRkkGK2PULJGEWS/0pc
h1286BOsydSM2Ai6+bnEbV0s/6X0YL4L3WlYxQgEkNuP
-----END CERTIFICATE-----
expiration      1501259623
issuing_ca      -----BEGIN CERTIFICATE-----
MIIFADCCAuigAwIBAgIUd0VBVb7dPA3fO8X36dt9LVhBpVcwDQYJKoZIhvcNAQEL
BQAwGDEWMBQGA1UEAxMNSE1DVFMgUm9vdCBDQTAeFw0xNzA3MjcxNTU3MzRaFw0x
...
<output truncated>
...
W47N/TSaO1kFNMFhE+QNeAzddp4SFrpoWrIZ1Z1mPo12Jl8aW89hzbj8CUHtv12t
6/U0lfBERcz13VzPl5pAfEWQs3/DJcfKJXVodkcMaD7BhDkk
-----END CERTIFICATE-----
serial_number   50:64:aa:f9:37:30:49:09:cb:b6:41:4f:e5:68:d2:ff:29:35:4f:99

/ #
```

Now we need to import the Root CA signed cert we created in the previous step back to the Intermediate CA backend. For this we copy the contents to a file `probate.crt`:

```code
/ # vault write hmcts_probate/intermediate/set-signed \
> certificate=@probate.crt
Success! Data written to: hmcts_probate/intermediate/set-signed
/ #
```

Using `curl` and `openssl` we can verify the contents of this certificate:

```code
/ # curl -s http://127.0.0.1:1234/v1/hmcts_probate/ca/pem | openssl x509 -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            20:e8:ca:3d:49:33:e6:b0:65:32:4e:9c:9a:84:a3:20:90:0c:ae:61
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=HMCTS Root CA
        Validity
            Not Before: Jul 27 16:54:40 2017 GMT
            Not After : Jul 28 16:55:10 2017 GMT
        Subject: CN=Probate Intermediate CA
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
                Modulus:
                    00:c1:03:35:7c:e4:a1:1b:00:7d:d4:62:0c:6b:47:
                    a1:79:a0:c7:a8:7e:9e:1d:0b:b1:90:6e:6a:cd:96:
...
<output truncated>
```

Just like we did with the Root CA, we can now configure the CA and CRL URLs for our Intermediate CA:

```code
/ # vault write hmcts_probate/config/urls \
> issuing_certificates="http://127.0.0.1/v1/hmcts_probate/ca" \
> crl_distribution_points="http://127.0.0.1/v1/hmcts_probate/crl"
Success! Data written to: hmcts_probate/config/urls
/ #
```

Before we can request certificates we should establish some restrictions around the certificates we generate like key types, ttl, etc ... For this we use the `role` functionality provided by vault:

```code
/ # vault write hmcts_probate/roles/frontend \
> key_bits=2048 \
> max_ttl=10h \
> allow_any_name=true
Success! Data written to: hmcts_probate/roles/frontend
/ #
```

and now we should be able to issue certs for this role:

```code
/ # vault write hmcts_probate/issue/frontend \
> common_name="test.probate.hmcts.net" \
> ip_sans="172.16.0.1" \
> ttl=5h \
> format=pem
Key                     Value
---                     -----
ca_chain                [-----BEGIN CERTIFICATE-----
MIIFjTCCA3WgAwIBAgIUIOjKPUkz5rBlMk6cmoSjIJAMrmEwDQYJKoZIhvcNAQEL
BQAwGDEWMBQGA1UEAxMNSE1DVFMgUm9vdCBDQTAeFw0xNzA3MjcxNjU0NDBaFw0x
NzA3MjgxNjU1MTBaMCIxIDAeBgNVBAMTF1Byb2JhdGUgSW50ZXJtZWRpYXRlIENB
...
<output truncated>

```

## Consequences
As demonstrated above, it is possible to use Vault as a Certification Authority. Vault's PKI backend offers enough flexibility to adapt the product to common demands for a CA.

It is important, however, to highlight that the values and names used in the examples above doesn't necessarily match the current names used in the Reform program. Likewise it is also important to mention that with this document we are not trying to provide guidance on how to operate Vault. Both of these last two points are outside of the scope of this ADR and should be covered in their own documentation due to the extensive nature of the topics.
