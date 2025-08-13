import shutil
from pathlib import Path
from typing import Union, Any

from fastapi import FastAPI, UploadFile, File, HTTPException, status, BackgroundTasks
from pydantic import BaseModel
import inspect


from common.util import Utility
from constants.constant import Constant
from request.processor import RequestEventTaskCommand
from fastapi import FastAPI, UploadFile, File
from io import StringIO
import pandas as pd
import os

from request.processor.processor_service import ProcessorService

app = FastAPI()

@app.post("/trigger-processing/", summary="Manually trigger background CSV file processing")
async def trigger_processing_pending_product_data():
    """
      Triggers the background process to scan the upload folder and process
      all pending CSV files in batches. The API call will return immediately.
      """
    processor_service = ProcessorService()
    try:
        result: dict = processor_service.process_all_pending_files_sync(Constant.UPLOAD_FOLDER, "API")
    except Exception as e:
        return {"message": f"Processing failed with an error: {e}"}
    else:
        return {"message": "Processing complete.", "summary": result.get("summary", [])}

@app.post("/upload-csv/", summary="Receive CSV Files and store for future batched processing")
async def upload_csv_file(file: UploadFile = File(...)):

    # 1. Ensure the file is a CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Please upload a CSV file."
        )

    # 2. Create data location if missing and define the path where the file will be saved
    Utility.check_if_dirs_exist(Constant.UPLOAD_FOLDER, True, True, )
    file_location = Path(Constant.UPLOAD_FOLDER) / file.filename

    try:
        # 3. Use shutil.copyfileobj to efficiently save the file
        with file_location.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # # 3. Read the file content and handle potential decoding errors
        # contents = await file.read()
        #
        # # 4. Decode bytes to a string and use StringIO to create a file-like object
        # s_io = StringIO(contents.decode('utf-8'))
        #
        # # 5. Use pandas to read the CSV into a DataFrame
        # df = pd.read_csv(s_io)
    # except UnicodeDecodeError as unicode_err:
    #     # The file content is not valid UTF-8
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail=(unicode_err, "Could not decode file content. Ensure it's a valid UTF-8 file.")
    #     )
    # except pd.errors.ParserError as pandas_err:
    #     # Malformed CSV, e.g., incorrect number of columns
    #     raise HTTPException(
    #         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    #         detail=(pandas_err, "The CSV file is malformed and could not be parsed.")
    #     )
    except Exception as ex:
        # Catch any other unexpected server-side errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=(ex, f"An unexpected error occurred while processing the CSV")
        )

    # Convert the DataFrame to a list of dictionaries
    # data_as_json = df.to_dict(orient="records")
    return {"message": f"File '{file.filename}' saved successfully!", "file_path": str(file_location)}
