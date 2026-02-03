from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_id = Column(Integer, ForeignKey("hcps.id"), nullable=False)

    raw_text = Column(Text, nullable=False)          # What user typed in chat
    summary = Column(Text, nullable=True)            # AI summarized text
    sentiment = Column(String(50), nullable=True)    # positive/neutral/negative
    follow_up = Column(String(255), nullable=True)   # next action
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship
    hcp = relationship("HCP")

    def __repr__(self):
        return f"<Interaction hcp_id={self.hcp_id}>"
