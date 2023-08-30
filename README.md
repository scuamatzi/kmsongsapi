# API for Kusimarka Songs.
### This API stores songs of kusimarka in json format in mongodb database.
This API was created using **FastAPI**

It has 4 endpoints: 
- First to provide a list of all songs in json mode
- Second to create a new record on database
- Third to update info of an existing record
- Fourth to delete a record

The credentials for database connection are stored in a file called `pass.json`. The structure of this file is like this:
```json
{
    "user":"user",
    "pass":"password",
    "uri":"URL"
}
```

## Run Locally

Get a mongodb database running, it could be with docker.

Update info in `pass.json`

In linux follow this steps inside the folder project (may use env):

```bash
pip install -r requirements.txt
```
```bash
uvicorn main:app --reload
```

Now the app runs on localhost:
```bash
http://localhost:8000/songs/
```

---------------------------


## Run on AWS Lambda

Get a mongodb database running on mongodb Atlas or other service.

Update data in `pass.json`

In linux follow this steps inside the folder project:

```bash
mkdir dep
```
```bash
pip install -t dep -r requirements.txt
```
```bash
cd dep
```
```bash
zip ../lambda_songs.zip -r .
```
```bash
cd ../
```
```bash
zip -r -u lambda_songs.zip database.py main.py model.py pass.json

```

Now create a lambda function on AWS and upload the file `lambda_songs.zip`

Be sure to enable "Function URL" and set it to NONE for authN for testing purposes.

After creation, change lambda handler to 'main.handler'

Add `/songs/` to AWS URL.
