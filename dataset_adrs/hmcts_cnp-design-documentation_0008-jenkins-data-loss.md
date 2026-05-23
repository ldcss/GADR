# 8. Azure IaaS disk encryption and data loss prevention
Date: 2017-10-31

## Status 
Proposal

## Context 

As per CNP-129: "Ensure no data loss for Jenkins down time", the requirements were to:

1.  Ensure no data loss for Jenkins down time
2.  Use a separate data drive for Jenkins
3.  Ensure that data drive has replication enabled
4.  Ensure that the data drive is backed up
5.  Ensure when the Jenkins box is rebuild, it mounts the (above) drive
6.  All data drives for IAAS should be encrypted
7.  manually Enable recovery VAULT for Jenkins

## Decision 

#### Data Loss

Currently, the terraform script to create the infrastructure creates an additional volume as a jenkins "data volume".  This resolves point 2) and partially resolves point 1) as block devices currently support Locally Redundant Storage (LRS) with data being replicated to at least 3 places within the same data center.
Originally, the intention was to use Azure Files (https://azure.microsoft.com/en-gb/services/storage/files/) in order to have an NFS volume attached, which would ease migration to a Jenkins PaaS offering.  However, given the current state of that technology, Azure Files does not provide Zone-redundant storage (ZRS) and so does not meet the requirement of point 3).

#### Encryption

In order to acheive the requirement for point 6), custom kernel modules are required to be installed on Linux systems to take advantage of the Azure Linux Agent (waagent) which communicates with the underlying hypervisor.  This is done during the Packer build of our base image, along with several other required packages.  As part of the bootstrap process for a Jenkins master, a script is installed and run to check for the presence of a data disk and configure it if required.  This script can be found here: https://raw.githubusercontent.com/contino/moj-module-jenkins/master/datadisk/datadisk.sh?token=AJ8ylGQJSftk3zecme9EPRtUupRalF5Kks5aAdmiwA%3D%3D

Unfortunately, due to the way the decryption of the disk seems to take place (a virtual CDROM is mounted with the credentials required to decrypt the disk), the VM never comes back online once it has been rebooted.

**A summary of this bahaviour has been sent to Microsoft and we are currently awating feedback.**


#### Backup

Creating a Recovery Vault and backup policy achieve the requirement for point 4).  Terraform currently does not support this operation natively, so a Azure Resource Manager template is used to create the vault (based on the azure-quickstart-templates).  This works successfully, however, creation of a Recovery Vault policy fails to create (both on the CLI and via the console).  Looking at the current API specification for a vault policy, it seems like much of the old functionality has been regressed.

**A summary of this bahaviour has been sent to Microsoft and we are currently awating feedback.** 


## Consequences

As a result of the issues listed above, the current solution supports 1) and 2) (given LRS data is stored in triplicate).  Decisions about encryption and backups will have to be made once Microsoft come back to us with fixes and/or workarounds.


## References

Linux Kernel Module download:
https://www.microsoft.com/en-us/download/details.aspx?id=55106&751be11f-ede8-5a0c-058c-2ee190a24fa6=True&e6b34bbe-475b-1abd-2c51-b5034bcdd6d2=True&fa43d42b-25b5-4a42-fe9b-1634f450f5ee=True

Azure Encryption Services:
https://docs.microsoft.com/en-us/azure/security/azure-security-disk-encryption

Encrypting disks on a Linux VM
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/encrypt-disks

Creating a vault
https://github.com/Azure/azure-quickstart-templates/tree/master/101-recovery-services-vault-create

Creating a vault policy
https://github.com/Azure/azure-quickstart-templates/tree/master/101-recovery-services-daily-backup-policy-create

Vault policy API definition
https://docs.microsoft.com/en-us/azure/templates/microsoft.recoveryservices/vaults/backuppolicies

