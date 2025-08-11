"""Model Class"""
from common.model import Status
from common.model.data_format import DataFormat

class RequestContext:
    """Stores data of current processing request, 
    used to track stages for retry
    """
    def __init__(self,
                 source: str,
                 data_format: DataFormat,
                 num_entries: int,
                 status: Status,
                 has_exception: bool,
                 is_partner_brand: bool,
                 brand: str
                 ):
        self.brand = brand
        self.is_partner_brand = is_partner_brand
        self.has_exception = has_exception
        self.status = status
        self.num_entries = num_entries
        self.format = data_format
        self.source = source
