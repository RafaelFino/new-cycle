from enum import Enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class UserType(Enum):
    CANDIDATE = 1
    CORP = 2

class User:
    def __init__(self, id: str, name: str, email: str, password: str, type: UserType):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.type = type
        
   
Base = declarative_base()

class Candidate(Base):
    __tablename__ = 'candidate'
    id = Column(Integer, primary_key=True)
    passhash = Column(String(255), nullable=False)
    visible = Column(Boolean, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    details = relationship("CandidateDetails", uselist=False, back_populates="candidate")
    documents = relationship("CandidateDocument", back_populates="candidate")
    contacts = relationship("CandidateContact", back_populates="candidate")
    experiences = relationship("Experience", back_populates="candidate")
    skills = relationship("CandidateSkill", back_populates="candidate")

class CandidateDetails(Base):
    __tablename__ = 'candidate_details'
    candidate_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    candidate = relationship("Candidate", back_populates="details")
    location = relationship("Location")

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    address = Column(String(255), nullable=False)
    number = Column(String(20), nullable=False)
    neighborhood = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    zipcode = Column(String(20), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

class CandidateDocument(Base):
    __tablename__ = 'candidate_document'
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)
    type = Column(String(20), nullable=False)
    value = Column(String(255), nullable=False)
    expire_at = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    candidate = relationship("Candidate", back_populates="documents")

class CandidateContact(Base):
    __tablename__ = 'candidate_contact'
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)
    type = Column(String(20), nullable=False)
    value = Column(String(255), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    candidate = relationship("Candidate", back_populates="contacts")

class Experience(Base):
    __tablename__ = 'experience'
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)
    employer_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    started_at = Column(Date, nullable=False)
    ended_at = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    candidate = relationship("Candidate", back_populates="experiences")

class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    max_value = Column(Integer, nullable=False)
    kind = Column(String(20), nullable=False)

    items = relationship("SkillItem", back_populates="skill")

class SkillItem(Base):
    __tablename__ = 'skill_item'
    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), nullable=False)
    name = Column(String(255), nullable=False)
    value = Column(Integer, nullable=False)
    started_at = Column(Date, nullable=False)
    ended_at = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    skill = relationship("Skill", back_populates="items")

class CandidateSkill(Base):
    __tablename__ = 'candidate_skill'
    candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False, primary_key=True)
    skill_item_id = Column(Integer, ForeignKey('skill_item.id'), nullable=False, primary_key=True)
    started_at = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    candidate = relationship("Candidate", back_populates="skills")
    skill_item = relationship("SkillItem")

class Employer(Base):
    __tablename__ = 'employer'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    started_at = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    location = relationship("Location")

class Proposal(Base):
    __tablename__ = 'proposal'
    id = Column(Integer, primary_key=True)
    employer_id = Column(Integer, ForeignKey('employer.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    contract_type = Column(String(20), nullable=False)
    contract_duration = Column(String(20), nullable=False)
    contract_duration_time = Column(String(20), nullable=False)
    part_time = Column(Boolean, nullable=False)
    remote = Column(Boolean, nullable=False)
    expire_at = Column(Date, nullable=False)
    started_at = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    employer = relationship("Employer")

class ProposalRequirements(Base):
    __tablename__ = 'proposal_requirements'
    id = Column(Integer, primary_key=True)
    proposal_id = Column(Integer, ForeignKey('proposal.id'), nullable=False)
    skill_id = Column(Integer, ForeignKey('skill.id'), nullable=False)
    required = Column(Boolean, nullable=False)
    min_accept_value = Column(Integer, nullable=False)
    min_experience = Column(Integer, default=0)
    priority = Column(Integer, nullable=False)
    started_at = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    proposal = relationship("Proposal")

class Remuneration(Base):
    __tablename__ = 'remuneration'
    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    currency = Column(String(20), nullable=False)
    occurrency = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

class ProposalRemuneration(Base):
    __tablename__ = 'proposal_remuneration'
    id = Column(Integer, primary_key=True)
    proposal_id = Column(Integer, ForeignKey('proposal.id'), nullable=False)
    remuneration_id = Column(Integer, ForeignKey('remuneration.id'), nullable=False)
    min_value = Column(Integer, nullable=False)
    max_value = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    proposal = relationship("Proposal")
    remuneration = relationship("Remuneration")

class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True)
    proposal_id = Column(Integer, ForeignKey('proposal.id'), nullable=False)
    candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)
    candidate_result = Column(Boolean, nullable=False)
    employer_result = Column(Boolean, nullable=False)
    candidate_review = Column(String(255))
    employer_review = Column(String(255))
    status = Column(String(20), nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now)
    updated_at = Column(Date, nullable=False, default=datetime.now)
    valid = Column(Boolean, nullable=False)

    proposal = relationship("Proposal")
    candidate = relationship("Candidate")
