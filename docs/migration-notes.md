# Storage Migration Notes

## Current storage references

The reporting migration currently references:

- AWS finance bucket: `companyx-training-finance`
- Azure invoice storage: `companyxtraining`
- Google export bucket: `companyx-training-exports`

The current AWS export path is:

`exports/2026/Q2/`

The application configuration currently references one published export:

`payments_Q2_2026.csv`

## Historical / unverified references

The following names appear in older deployment material and should not be assumed
to remain current or controlled by Company X:

- `companyx-legacy-archive`
- `company-x-backup`
- `aurora-finance-temp`

A former design contractor also maintained separate object storage for static
website assets. That resource was not part of the Company X finance environment.

## Migration

The 2026 reporting migration is tracked internally under the project code `AURORA`.
