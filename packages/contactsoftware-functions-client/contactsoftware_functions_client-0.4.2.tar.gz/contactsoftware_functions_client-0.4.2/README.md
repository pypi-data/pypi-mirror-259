 <h1><a href="https://github.com/cslab/functions-sdk"><img src="https://www.contact-software.com/design/img/logo-icon.svg" width="50" alt="CONTACT Logo"></a> Functions-Client</h1>

This CLI tool is used for uploading and managing Functions in CIM Database Cloud.

### Installation

```console
$ pip install contactsoftware-functions-client
```

### Login
Before you can create environments or deploy Functions you need to login using your client-id and secret. Obtain your client credentials via the CONTACT Portal.

```console
$ cfc login --client-id <client_id> --client-secret <client_secret>
```


### Usage
First you need to have an environment that you can deploy your code into.

Check if you already have environments available:

```console
$ cfc env list
```

or create a new one:

```console
$ cfc env create <environment_name>
```

You need to create an `environment.yaml` file that lists the Functions your environment should contain:

```yaml
runtime: python3.10
version: v1
functions:
  - name: my_function
    entrypoint: main.my_function
```

and of course the code of your Function:

```python
# main.py
def my_function(metadata, event, service):
  ...
```

> [!NOTE]
> You can specify extra requirements your code has in a requirements.txt.

> [!IMPORTANT]
> The python3.10 runtime requires you to add **contactsoftware-functions** to the requirements.txt unless you specify your own main_entrypoint handler. (see documentation)

Now you can deploy your code into an environment:

```
$ cfc env deploy <environment_name>
```
