# Accessing Microsoft Access Database Using a Mac 

**Status:** Accepted

## Context

Our client has a Microsoft Access Database locally which they use to view and manipulate their data. The app that we have built for them exports CSVs to upload to that Access DB. Microsoft Access is purely a Windows application however, and there is no Mac version available. So that we can use the MDB schema that the client has sent over, we had a look at the following options. 

### Option 1 - Find an alternative MDB tool for Mac

We looked at several alternative options including Dbeaver, LibreOffice Base, and MDB ACCDB viewer, but all of them lacked some functionality and some were paid apps. 


### Option 2 - Use a Virtual Machine Emulator

There were several options for VM Windows emulators, but at the time of our engagement, most of our team members were using Mac’s with M1 chips, and ‘Parallels’ was the only VM with compatibility for the new Mac M1 chips.

## Final Decision

We decided to go for option 2, as it offers full functionality. Once downloading Windows on this, we were able to download Microsoft Office, which when downloaded on Windows, includes a version of Microsoft Access.  
