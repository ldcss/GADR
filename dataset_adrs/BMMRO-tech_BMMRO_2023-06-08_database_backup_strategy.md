# Database Backup Strategy

**Status:** Accepted

## Context

Currently we do not have a backup of the firestore database. We would ideally like to back up the data in production every day, so that we can restore the database in case of any issues.

## Assumptions

1  We are assuming by entering long comments, quotes, etc.that single record (forms) will not exceed 3.5 KB in size approx according to the client 100 forms a year means the total size needed to store the form data will not exceed 0.4MB (3.5 *100) a year plus the admin overhead (security etc). Since the data is exported and compressed for backup, daily storage requirements will not exceed 0.2MB a day or 6 MB a month. After 30 days backup files will be deleted automatically as per GCP’s policy on cost-free option.

2  Video recordings and audio recordings kept in the site(links) but not in cloud storage.

3  We are not concerned with storing the videos, audios and images as they are stored in dropbox, the db will contain only the references which are urls.

## Decision

We decided to use export function from firestore and then use GitHub Actions to automate backup of firebase database.

These were the different options considered for the database backup strategy:

### Option 1 - Import/ Export firestore data manually

We can use the Cloud Firestore managed export and import service to recover from accidental deletion of data for offline processing. However this would require a manual intervention every time the data needs to be exported.

Pros:
- Readily available

Cons:
- This would be a manual step by step export of the data every day.
- Time-consuming 

### Option 2 - Automate the import/ export of firestore data using github workflow

Github actions can be used to automate the export function for firestore. We will be using the google apis and the exported data will be stored in the gcp buckets.

Pros:
- Provides automated exports.
- Great configuration flexibility.
- Uses the configuration of a Cron job which will automate the backup recovery in sec/min/hours/day/week
- Supports exports via gcloud CLI
- Facilitates various levels of granularity
- Fast, easy to follow and implement

### Option 3 - Automated Firebase backup

This approach is about automated backup using blaze plan which can then be used for restoring from backups using import and scheduling. This approach refers to Firebase Realtime Database for automatic backups but this project is using Firestore database.


# Final Decision

We have decided to go ahead with Option 2. Github workflow with a cron job will be run every day to automate the export of the firestore data. The data will then be stored in the gcp storage buckets. In case of disaster recovery, the import will have to be done manually.


# Backup Recovery

Due to various considerations regarding the cost, time consumption and effort, it has been decided that the backup recovery, should it be needed, is performed manually, by following the steps detailed in the document:

https://docs.google.com/document/d/1cLcZQ02GPC5HHhI_QSGX96U3baU3XyCl8zgMB1j8D7s/edit#heading=h.pewbr289rkwh


