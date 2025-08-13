import os
import csv

from sqlalchemy.orm import Session, sessionmaker

from common.model.domain_model import RequestContext
from common.model.domain_model.enum import Status, DataFormat
from common.model.domain_model.enum.partner_brand import PartnerBrand
from config import DatabaseManager
from exception import ProcessorServiceException
from request.processor import RequestEventTaskCommand

class ProcessorService:
    def __init__(self):
        pass

    @classmethod
    def process_all_pending_files_sync(cls, upload_folder: str, service_name: str = "CRON_JOB") -> dict:
        """
        Synchronous function to process all CSV files in the upload folder.
        Designed to be run as a background task.
        """
        print(f"Processing task triggered. Scanning {upload_folder}...")
        files_to_process = [f for f in os.listdir(upload_folder) if f.endswith('.csv')]
        if not files_to_process:
            raise ProcessorServiceException({cls.__class__.__name__: "No CSV files found for processing!"})
        processing_summary = []
        session_local: sessionmaker[Session] = DatabaseManager.get_session_local() # Get the session factory once         print(f"files_to_process {files_to_process}")
        for filename in files_to_process:
            file_path: str = os.path.join(upload_folder, filename)
            file_results = {"filename": filename, "total_records": 0, "successful_records": 0, "failed_records": 0}

            try:
                with open(file_path, 'r', newline='') as f:
                    request_context = cls.get_request_context(f, file_path)
                    for chunk in cls.process_csv_in_chunks(f, chunk_size=100):
                            for record_data in chunk:
                                file_results["total_records"] += 1
                                db_session: Session = session_local() # Create a new session for each record
                                task_command = RequestEventTaskCommand(service_name)
                                try:
                                    data = {"context": request_context}
                                    task_command.execute(data, db_session)
                                    # db_session.commit() # Commit changes for this record
                                    file_results["successful_records"] += 1
                                except Exception as e:
                                    file_results["failed_records"] += 1
                                    print(
                                        f"Record processing failed for '{record_data.get('id', 'N/A')}' in '{filename}': {e}")

                # new_file_path = os.path.join(processed_folder, filename)
                # shutil.move(file_path, new_file_path)
                file_results["status"] = "processed"
                # print(f"Successfully processed and moved '{filename}' to {processed_folder}")

            except Exception as e:
                db_session.rollback() # Rollback on any error for this record
                # new_file_path = os.path.join(error_folder, filename)
                # shutil.move(file_path, new_file_path)
                file_results["status"] = "failed"
                file_results["error_message"] = str(e)
                # print(f"File '{filename}' failed entire processing due to: {e}. Moved to {error_folder}")
            finally:
                db_session.close() # Always close the session

            processing_summary.append(file_results)

        print("Background processing task completed.")
        return {"summary": processing_summary}


    @classmethod
    def process_csv_in_chunks(cls, file, chunk_size=100):
        reader = csv.DictReader(file)
        chunk = []
        for i, row in enumerate(reader):
            chunk.append(row)
            if (i + 1) % chunk_size == 0:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

    @classmethod
    def get_request_context(cls, file_path, file_name) -> RequestContext:
        source = file_name
        data_format = DataFormat.CSV
        num_entries = cls.get_entries_in_file(file_path)
        status = Status.ARRIVED
        has_exception = False
        is_partner_brand = cls.is_known_partner_brand(cls.get_brand_name())
        brand = cls.get_brand_name()
        return RequestContext(source, data_format, num_entries, status, has_exception, is_partner_brand, brand)


    @classmethod
    def get_entries_in_file(cls, file) -> int:
        """
        Counts the number of records in a CSV file-like object and
        resets the file pointer to the beginning.
        """
        reader = csv.DictReader(file)
        count = sum(1 for _ in reader)
        # after seek, need to revert cursor to beg
        file.seek(0)
        return count - 1 # take into account the header

    # TODO: IMPLEMENT
    @classmethod
    def get_brand_name(cls) -> str:
        return ""

    @classmethod
    def is_known_partner_brand(cls, brand_name: str) -> bool:
        return PartnerBrand.has_value(brand_name)
