import logging

import azure.functions as func

import hashlib

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    md5_to_hash = req.params.get('str')
    if not md5_to_hash:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            md5_to_hash = req_body.get('str')

    if md5_to_hash:
        return func.HttpResponse(hashlib.md5(md5_to_hash.encode('utf-8')).hexdigest() )
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
