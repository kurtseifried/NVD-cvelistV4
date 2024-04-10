# NVD-cvelistV4

This is the NVD data (https://nvd.nist.gov/vuln/data-feeds) broken up into JSON files in CVE JSONv4 format (https://github.com/CVEProject/cve-schema/tree/master/schema/v4.0) and the same layout as the CVE v5 repo (https://github.com/CVEProject/cvelistV5) which is /cve/YEAR/Nxxx/CVE-YEAR-NUMBER.json. Please note this is effectively trhe same as the CVE v4 repo, but with the /cve/ directory at the root.

## Workflow

0-process-all.sh runs git commands and both the 1-initial-download-process.sh and 2-update-download-process.sh scripts.

0-process-new.sh just runs the 2-update-download-process.sh script.

The 1-initial-download-process.sh gets the CVE-YEAR gzip files from the NVD. The 2-update-download-process.sh gets just the CVE-Modified and CVE-Recent which are the last 10 days or so of activity.

In other words if it has been less than 10 days since the repo was updated just run the 0-process-new.sh and if it has been 10 or more days since the last update run the 0-process-all.sh. Please note that 0-process-all.sh takes about 60 minutes to run in a VM due to the size and use of "git add -A" which ensures we get all the files.

## TODO

Set a calendar reminder to update this weekly?
Rebuild the VM that updates all those GitHub repos and automate this?
