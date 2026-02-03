from sqlalchemy import Column, Integer, String
from database.db import Base

class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    hospital = Column(String(255), nullable=True)
    specialty = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<HCP name={self.name}>"
