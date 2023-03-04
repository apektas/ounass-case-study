from app.database import Base
from sqlalchemy import String, Integer, Column, DateTime, Sequence
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime


class Campaign(Base):
    __tablename__ = 'campaigns'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    objective = Column(String, nullable=True)
    status = Column(String, nullable=True)
    time_created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Campaign id={self.id} name={self.name} objective={self.objective}>"


class AdSet(Base):
    __tablename__ = 'ad_sets'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    campaign_id = Column(String, nullable=False)
    daily_budget = Column(String, nullable=True)
    start_time = Column(DateTime, default=datetime.utcnow, nullable=True)
    end_time = Column(DateTime, nullable=True)
    targeting = Column(JSON, nullable=True)
    bid_amount = Column(Integer, nullable=True)
    status = Column(String, nullable=True)
    optimization_goal = Column(String, nullable=True)

    def __repr__(self):
        return f"<AdSet id={self.id} name={self.name} campaign_id={self.campaign_id} status={self.status}>"


class AdImage(Base):
    __tablename__ = 'ad_images'
    id = Column(Integer, Sequence('id', start=1, increment=1), primary_key=True)
    name = Column(String, nullable=True)
    hash = Column(String, nullable=True)
    url = Column(String, nullable=True)


class AdCreative(Base):
    __tablename__ = 'ad_creatives'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    object_story_spec = Column(JSON, nullable=True)


class Ad(Base):
    __tablename__ = 'ads'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    creative = Column(JSON, nullable=True)
    status = Column(String, nullable=True)
    adset_id = Column(String, nullable=False)


