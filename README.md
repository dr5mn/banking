# banking
Basic script to interact with the Investec API

The scripts are set up to run in their own folders, e.g.

/Investec
    /Get Info
        GetAccounts...
        GetTransactions.py
        GetTransactionsInc.py
    /Analyse
        ScriptsForAnalysingData
    /Config
        config.json
        sandbox_config.json
    /Output
        /Accounts
        /Transactions
        /TransactionsCSV

An example of config.json would look like this:

{
    "host" : "the.prod.url",
    "client_id" : "your.client.id",
    "client_secret" : "your.secret",
    "acc_id" : "your.acc.id",
    "main_api_key" : "your.primary.api.key",
    "alt_api_key" : "a.backup.api.key",
    "auth_base64" : "the.base64.version.of.clientid.and.clientsecret"
}

sandbox_config.json looks like this:

This info is publically available on Investec's API documentation. Please consult their developer website to obtain this info.

{
    "host" : "the.sandbox.url",
    "client_id" : "the.testing.client.id",
    "client_secret" : "the.testing.client.secret",
    "api_key" : "the.testing.api.key",
    "auth_base64" : "the.testing.base64"
}

