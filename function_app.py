""" Python AzureFUnction to add a watermark to a PDF file
"""
import logging
import azure.functions as func


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="WatermarkV1")
def WatermarkV1(req: func.HttpRequest) -> func.HttpResponse:
    """ HTTP Trigger function to add a watermark to a PDF file"""
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed.")
    else:
        return func.HttpResponse(
             "This V2 HTTP triggered function executed successfully. Pass a name for a response.",
             status_code=200
        )
        