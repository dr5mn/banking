# Investec API interaction

These are some basic scripts to interact with the Investec API. It let's you get transactions, by either specifying a date range, or by extracting multiple ranges in a loop, incrimentally.

More scripts will be added later, e.g. to extract account details. 

**Folder structure**

The scripts are set up to run in their own folders, e.g.

* /Investec
    * /Get Info
        * GetAccounts...
        * GetTransactions.py
        * GetTransactionsInc.py
    * /Analyse
        * ScriptsForAnalysingData
    * /Config
        * config.json
        * sandbox_config.json
    * /Output
        * /Accounts
        * /Transactions
        * /TransactionsCSV

**Config**

*Main config*

An example of config.json would look like this:

```
{
    "host" : "the.prod.url",
    "client_id" : "your.client.id",
    "client_secret" : "your.secret",
    "acc_id" : "your.acc.id",
    "main_api_key" : "your.primary.api.key",
    "alt_api_key" : "a.backup.api.key",
    "auth_base64" : "the.base64.version.of.clientid.and.clientsecret"
}
```

*Sandbox config*

sandbox_config.json looks like this:

This info is publically available on Investec's API documentation. Please consult their developer website to obtain this info.
```
{
    "host" : "the.sandbox.url",
    "client_id" : "the.testing.client.id",
    "client_secret" : "the.testing.client.secret",
    "api_key" : "the.testing.api.key",
    "auth_base64" : "the.testing.base64"
}
```
