import logging
import azure.functions as func
from WatermarkV1.watermark import add_watermark

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    Approver = req.params.get('Approver')
    PDF_Path = req.params.get('PDF_Path')
    Out_Path = req.params.get('Out_Path')

    if not Approver or not PDF_Path:
        return func.HttpResponse(
            "Please pass Approver and PDF_Path in the query string or in the request body",
            status_code=400
        )

    try:
        add_watermark(PDF_Path, Approver, Out_Path)
        return func.HttpResponse(f"Watermark added successfully to {PDF_Path}.")
    except Exception as e:
        logging.error(f"Error adding watermark: {e}")
        return func.HttpResponse(
            f"Error adding watermark: {e}",
            status_code=500
        )
