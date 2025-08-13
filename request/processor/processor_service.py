import os
import csv
import shutil
from typing import Any, Dict, List


class ProcessorService:
    def __init__(self):
        pass

    @classmethod
    def process_csv_in_chunks(self, file, chunk_size=100):
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
    def process_all_pending_files_sync(self, upload_folder: str, processed_folder: str, error_folder: str):
        """
        Synchronous function to process all CSV files in the upload folder.
        Designed to be run as a background task.
        """
        print(f"Background processing task started. Scanning {upload_folder}...")

        files_to_process = [f for f in os.listdir(upload_folder) if f.endswith('.csv')]

        if not files_to_process:
            print("No CSV files found for processing.")
            return {"message": "No files to process."}

        processing_summary = []

        for filename in files_to_process:
            file_path = os.path.join(upload_folder, filename)
            file_results = {"filename": filename, "total_records": 0, "successful_records": 0, "failed_records": 0}

            try:
                with open(file_path, 'r', newline='') as f:
                    for chunk in self.process_csv_in_chunks(f, chunk_size=100):
                        for record_data in chunk:
                            file_results["total_records"] += 1
                            context = RequestContext(record=record_data)
                            task_command = RequestEventTaskCommand()

                            try:
                                task_command.execute(context)
                                file_results["successful_records"] += 1
                            except Exception as e:
                                file_results["failed_records"] += 1
                                print(
                                    f"Record processing failed for '{record_data.get('id', 'N/A')}' in '{filename}': {e}")

                new_file_path = os.path.join(processed_folder, filename)
                shutil.move(file_path, new_file_path)
                file_results["status"] = "processed"
                print(f"Successfully processed and moved '{filename}' to {processed_folder}")

            except Exception as e:
                new_file_path = os.path.join(error_folder, filename)
                shutil.move(file_path, new_file_path)
                file_results["status"] = "failed"
                file_results["error_message"] = str(e)
                print(f"File '{filename}' failed entire processing due to: {e}. Moved to {error_folder}")

            processing_summary.append(file_results)

        print("Background processing task completed.")
        return {"message": "Processing finished.", "summary": processing_summary}
