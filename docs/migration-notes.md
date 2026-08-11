# Storage Migration Notes

## Current references
- Finance reports: `https://companyx-training-finance.s3.amazonaws.com/reports/`
- Approved invoices: `https://companyxtraining.blob.core.windows.net/invoices/`
- Analytics exports: `https://storage.googleapis.com/companyx-training-exports/quarterly/`

## Historical / unverified references
The following names were found in old deployment notes and should not be assumed to
remain associated with Company X:
- `companyx-legacy-archive`
- `company-x-backup`
- `aurora-finance-temp`

A third-party design contractor previously used its own object storage for static
website imagery. That storage is not a Company X finance resource.

## Migration
Project Aurora is expected to move approved reporting artefacts into the consolidated
finance archive.
