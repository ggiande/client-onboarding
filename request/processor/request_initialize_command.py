from overrides import overrides
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError

from common.model import RequestContext
from common.model.data_model import MHGTProductDetail
from common.model.domain_model.enum import Status
from common.processor.initialize_command_base import InitializeCommandBase
from exception import RequestDataValidationException


class RequestInitializeCommand(InitializeCommandBase):

    def __init__(self, service_name: str):
        self.service_name = service_name


    @overrides
    def is_command_applicable(self, data: dict) -> bool:
        return True

    def execute(self, data: dict, db_session: Session) -> dict:
        """
        assert source, assert format, assert number of entries to be processed in the batch,
        brand name, isPartnerBrand, status, hasExceptions
        :param db_session:
        :param data:
        :return: modified data
        """
        if not self.is_command_applicable(data):
            return data
        print(f"Executing {self.__class__.__name__} for service {self.service_name}")

        errors = {}

        req_context: RequestContext = data["context"]
        if not req_context:
            errors[self.__class__.__name__] = "No Request Context Found!!! Bug in the code?"

        new_transaction_record = MHGTProductDetail(
            brand = req_context.brand,
            created_by = self.service_name,
            data_format = req_context.data_format,
            has_exception = req_context.has_exception,
            is_partner_brand = req_context.is_partner_brand,
            num_entries = req_context.num_entries,
            perf_dupe_checked = False,
            source_data= req_context.source_data,
            status = req_context.status,
            updated_by = self.service_name,
        )

        try:
            db_session.add(new_transaction_record)
            db_session.commit()
        except UnmappedInstanceError as err:
            errors[self.__class__.__name__] = err
        else:
            data['transaction_id'] = new_transaction_record.id

        req_context.status = Status.IN_PROGRESS

        if errors:
            req_context.status = Status.ERROR
            req_context.has_exception = True
            raise RequestDataValidationException(errors)

        print("Initializing the request...")
        return data


    # CREATE TABLE MHGT_PRODUCT_DETAIL(
    #     id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    # created_dttm TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    # updated_dttm TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    # --	APPLICATION DATA
    # brand VARCHAR(500),
    # created_by VARCHAR(75),
    # data_format VARCHAR(20),
    # has_exception BOOLEAN,
    # is_partner_brand BOOLEAN,
    # num_entries INTEGER,
    # perf_dupe_checked BOOLEAN,
    # source_data VARCHAR(255),
    # status VARCHAR(50),
    # updated_by VARCHAR(75)
    # );

