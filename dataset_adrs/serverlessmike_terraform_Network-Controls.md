# Disable Defender

Date: 14/01/2020

## Context

- Windows Defender is active by default in the Windows Server 2019 AMIs shipped by AWS. Although there is a good deal of overlap between the functionality of AWS Security Groups and Windows Defender, AWS has decided to keep Defender active for one specific reason, namely; "the Windows firewall gives you audit details about packet drops, which may be important to meet your security policy or compliance requirements". There is currently no such requirement in RI Tech.
- Windows Defender is difficult, but not impossible, to configure in code. 
- AWS Security Groups are relatively easy to configure in code.
- When Defender is in use, the best way to work out what it is doing, is to log into the instance as Administrator and use the Defender GUI, but logging in as Administrator is strongly discouraged.

## Decision

Windows Defender is to be de-activated on all Windows Servers in AWS.

## Consequences

Every Windows instance in AWS must be in security groups that allow only the minimal set of inbound traffic. Ports and protocols that are not required for normal operations are to be blocked.
