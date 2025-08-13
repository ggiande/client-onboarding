from common.model.domain_model.enum import DataFormat, Status

from sqlalchemy import Column, String, Boolean, Integer, Enum, UUID, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

# Declarative base is NEEDED for sqlAlchemy ig
Base = declarative_base()

class MHGTProductDetail(Base):
    __tablename__ = 'mhgt_product_detail'

    # DB Gen
    id = Column(UUID, primary_key=True, server_default=func.gen_random_uuid())
    created_dttm = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_dttm = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

    # Application data
    brand = Column(String(500))
    created_by = Column(String(75))
    data_format = Column(Enum(DataFormat), nullable=False)
    has_exception = Column(Boolean)
    is_partner_brand = Column(Boolean)
    name = Column(String(1000))
    num_entries = Column(Integer)

    # The column name from SQL is perf_dupe_checked
    perf_dupe_checked = Column(Boolean)
    source_data = Column(String(255))
    status = Column(Enum(Status), nullable=False)
    updated_by = Column(String(75))

    # REPR is for devs, __STR__ is for client facing
    def __repr__(self):
        return f"<MHGTProductDetail(id='{self.id}', status='{self.status}')>"
