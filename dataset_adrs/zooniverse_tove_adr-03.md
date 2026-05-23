# ADR 03: Azure Data Storage Tools

* Status: Approved
* Date: Jan 16 2020

## Context

When a transcription is approved, a set of flat files containing the transcription data will be saved to Azure. Users will have the option to download a zip file containing their requested subject, group, workflow, or project. Depending on the speed at which we are able to zip the necessary files, we will either trigger a direct download, or provide a link to the location of the zip file to the user. 

The goal is to investigate Azure’s storage options (specifically Blob Storage and File Services) and decide which tool is best suited for our needs.

### Factors to consider:

* How easy is it to share a file to the end user? What is the process for this?
* Ease of use, how complicated is it to set up, maintain, edit
* access permission features
* Speed of accessing and iterating through files (e.g. getting all files in a given directory)

### Terminology:

**Blob:** acronym for “Binary Large Object”  
**Container:** synonym for ”S3 Bucket”  
**Shared Access Signature:** similar functionality as “S3 Presigned URLs”

## Considered Options

* Blob Storage
* File Services

> Azure Files and Azure Blob Storage both offer ways to store large amounts of data in the cloud, but they are useful for slightly different purposes.
>
> Azure Blob Storage is useful for massive-scale, cloud-native applications that need to store unstructured data. To maximize performance and scale, Azure Blob Storage is a simpler storage abstraction than a true file system. You can access Azure Blob Storage only through REST-based client libraries (or directly through the REST-based protocol).
>
> Azure Files is specifically a file system. Azure Files has all the file abstracts that you know and love from years of working with on-premises operating systems. Like Azure Blob Storage, Azure Files offers a REST interface and REST-based client libraries. Unlike Azure Blob Storage, Azure Files offers SMB access to Azure file shares. By using SMB, you can mount an Azure file share directly on Windows, Linux, or macOS, either on-premises or in cloud VMs, without writing any code or attaching any special drivers to the file system. You also can cache Azure file shares on on-premises file servers by using Azure File Sync for quick access, close to where the data is used.

Both options allow for specifying read-only or write-only permissions on folders or files using [Shared Access Signatures](https://docs.microsoft.com/en-us/rest/api/storageservices/create-user-delegation-sas).

### Option 1: Azure Blob Storage

#### Summary 
Blob Storage is optimized for storing unstructured data: e.g. information that doesn't reside in a traditional row-column database. Blobs come in [three different types](https://docs.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs): block blobs, append blobs, and page blobs.

##### Block Blobs
 A block blob consists of one or more blocks, each each of which is identified by a block ID. 

By default, storage clients limit block size to 128 MB, such that when a block blob upload is more than 128 MB, the file will be broken into several blocks. This maximum block size can be updated via the SingleBlobUploadThresholdInBytes property. 

When uploading additional blocks to a blob, the additional blocks are associated with the specified blob, but do not become part of the blob until you commit a list of block IDs that include the newly uploaded blocks.

The [azure-storage-blob gem](https://github.com/azure/azure-storage-ruby/tree/master/blob) allows us to talk to Azure blob storage using ruby methods, though it only provides functionality for working with block blobs (to work with any other type of blob, we would have to construct HTTP requests by hand). The gem methods abstract away the interaction with individual blocks within a blob, and automatically creates multiple blocks (all associated with a single blob) if the file is greater than the maximum size allowed for a single block.

##### Append Blobs 
An append blob also consists of one or more blocks, but is optimized for appending additional blocks onto the blob. Blocks can only be added to the end of an append blob, and block IDs are not exposed.

##### Page Blobs
>Page blobs are a collection of 512-byte pages optimized for random read and write operations.

Page blobs are initialized with a maximum data size, and updated by by specifying an offset and a range that match up with the 512-byte page boundaries.

#### Specs
Target throughput for a single blob is up to 60 MiB per second

#### Pros:
- Blob Storage has been around for longer (appears to have shipped with the original launch of Azure Web Services in 2010), which means there will be more existing conversation around it (e.g. on stack overflow) and more tools/plugins for working with it
- User reviews present Blob Storage as the go-to option, with File Services being an alternative that is employed for use cases that require specific additional functionality provided by File Services (e.g. lifting and shifting an existing file system)
- Offers a simpler, more basic solution
- Blob Storage is much cheaper than file storage (approximately 1/5 of the cost per unit of data)
- Greater maximum storage size than file storage (2PiB: 1 PiB = 2^50 bytes)

#### Cons: 
- Directory hierarchy system within blob storage is purely virtual - that is, a directory is merely an abstraction over the `/`-delimited names of the underlying container/blob hierarchy. In other words, a virtual directory is a prefix that you apply to a file (blob) name. We should note that AWS S3 service works the same, i.e. there is a storage account, there are buckets (containers), and then stores objects (blobs) using a prefix notation just like you would in blob storage.

### Option 2: Azure File Service

#### Specs
Target throughput for a single file share: up to 300 MiB/sec for certain regions, Up to 60 MiB/sec for all regions

#### Pros: 
- can cache Azure file shares on on-premises file servers by using Azure File Sync for quick access
- File Services uses the SMB protocol, which is the same protocol used on file directories on Mac and Windows machines. Therefore a file share can be mapped onto a drive on your machine. Note that a blob container can also be mounted as a file system using the [blobfuse](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux) tool, so this is not an actual advantage over Blob Storage.
- Greater potential throughput

#### Cons:
- Launched in Sept 2015, hasn't been around for as long as Blob Storage.
- Smaller max size (100 TiB: 1 TiB = 2^40 bytes). We are not expecting to come close to this size, so this isn’t much of a concern

## Decision

We don't appear to have any need for most of the additional functionality that comes with File Service, which makes me reluctant to want to use it. In addition, the number of articles and resources available on communicating with Blob Storage to set up file zipping is much greater than what's available for File Service. My initial understanding of Blob Storage led me to believe that permissions could only be set at the container level, but this turned out to be wrong. With the ability to set blob-specific permissions, we will be able to use a single container to store the transcription-specific files, and the user-requested zip files.

Ultimately, my choice is to go with Blob Storage: the more basic, simple storage tool that gives us what we need and nothing more. That being said, I'd still like to keep the option of using Azure File Service on the table, in case it turns out that we *would* benefit from the additional functionality that it offers.

As for what type of blob we will use, my choice would be to store each data file in its own block blob. If we were to choose to store multiple files within a single blob (and have each file be associated with a block ID on that blob), we would lose the ability to name each individual file. Hypothetically, it would be possible to create a database table with columns “block ID” and “name”, to emulate a naming functionality, but this seems far more complicated than its worth. In addition, the [azure-storage-blob](https://github.com/azure/azure-storage-ruby/tree/master/blob) gem gives us a simple interface for working with block blobs and saves us the trouble of having to write HTTP requests ourselves.

Final questions:
1. Q: Blob Storage doesn't have any concrete hierarchy beyond Storage Account/Blob Container - within a container, directories are virtual, demarcated by prefixes in the file name. Will this end up being problematic for us? Will it complicate file retrieval?  
A: Retrieving files from a file system with virtual directories shouldn't be any different than retrieving files from a normal file system. As long as blob prefixes are constructed in a way that reflects the organizational system used within the application/database, there should be no trouble. File retrieval may be helped by append blobs - final decision on blob type is still TBD.

2. Q: Would there be any benefit to caching files on on-premises file servers? If this sounds like something we'd like to employ, it would be worth reconsidering Azure File Service.
A: This doesn't appear to be something we will need.


### Links and Articles:
1. [Microsoft: Deciding when to use Azure Blobs, Azure Files, or Azure Disks](https://docs.microsoft.com/en-us/azure/storage/common/storage-decide-blobs-files-disks)
2. [Azure Files FAQ](https://docs.microsoft.com/en-us/azure/storage/files/storage-files-faq) (see ‘Why would I use an Azure file share versus Azure Blob Storage for my data?’) 
3. [Stack Overflow: Blob Storage vs File Service](https://stackoverflow.com/questions/24880430/azure-blob-storage-vs-file-service)
4. [Microsoft: Introducing Azure File Service](https://blogs.msdn.microsoft.com/windowsazurestorage/2014/05/12/introducing-microsoft-azure-file-service/) (scroll to When to use Azure Files vs Azure Blobs vs Azure Disks)
5. [Microsoft: Azure Storage scalability and performance targets for storage accounts](https://docs.microsoft.com/en-us/azure/storage/common/storage-scalability-targets)
6. [Azure Blob Overview](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview)
7. [Azure Blob Introduction](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
8. [How to mount Blob storage as a file system with blobfuse](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux)
9. [Block blobs, append blobs, and page blobs](https://docs.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs)
10. [Azure Blob Storage gem](https://github.com/azure/azure-storage-ruby/tree/master/blob)
