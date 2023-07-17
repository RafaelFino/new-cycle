CREATE TABLE Candidate (
    ID SERIAL PRIMARY KEY,
    PassHash VARCHAR(255) NOT NULL,
    Visible BOOLEAN NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,    
);

CREATE TABLE CandidateDetails (
    CandidateID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    LocationID VARCHAR(255) NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (CandidateID) REFERENCES Candidate (ID),
    FOREIGN KEY (LocationID) REFERENCES Location (ID)
);

CREATE TABLE Location (
    ID SERIAL PRIMARY KEY,
    Address VARCHAR(255) NOT NULL,
    Number VARCHAR(20) NOT NULL,
    Neighborhood VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL,
    State VARCHAR(255) NOT NULL,
    City VARCHAR(255) NOT NULL,
    ZipCode VARCHAR(20) NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL
);

CREATE TABLE CandidateDocument (
    ID SERIAL PRIMARY KEY,
    CandidateID INT NOT NULL,
    Type VARCHAR(20) NOT NULL,
    Value VARCHAR(255) NOT NULL,
    ExpireAt DATE NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (CandidateID) REFERENCES Candidate (ID)
);

CREATE TABLE CandidateContact (
    ID SERIAL PRIMARY KEY,
    CandidateID INT NOT NULL,
    Type VARCHAR(20) NOT NULL,
    Value VARCHAR(255) NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (CandidateID) REFERENCES Candidate (ID)
);

CREATE TABLE Experience (
    ID SERIAL PRIMARY KEY,
    CandidateID INT NOT NULL,
    EmployerName VARCHAR(255) NOT NULL,
    Description TEXT NOT NULL,
    StartedAt DATE NOT NULL,
    EndedAt DATE NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (CandidateID) REFERENCES Candidate (ID)
);

CREATE TABLE Skill (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    MaxValue INT NOT NULL,
    Kind VARCHAR(20) NOT NULL
);

CREATE TABLE SkillItem (
    ID SERIAL PRIMARY KEY,
    SkillID INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Value INT NOT NULL,
    StartedAt DATE NOT NULL,
    EndedAt DATE NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (SkillID) REFERENCES Skill (ID)
);

CREATE TABLE CandidateSkill (
    CandidateID INT NOT NULL,
    SkillItemID INT NOT NULL,
    StartedAt DATE NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (CandidateID) REFERENCES Candidate (ID),
    FOREIGN KEY (SkillItemID) REFERENCES SkillItem (ID)
);

CREATE TABLE Employer (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    LocationID VARCHAR(255) NOT NULL,
    StartedAt DATE NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (LocationID) REFERENCES Location (ID)    
);

CREATE TABLE Proposal (
    ID SERIAL PRIMARY KEY,
    EmployerID INT NOT NULL,
    Title VARCHAR(255) NOT NULL,
    Description TEXT NOT NULL,
    ContractType VARCHAR(20) NOT NULL,
    ContractDuration VARCHAR(20) NOT NULL,
    ContractDurationTime VARCHAR(20) NOT NULL,
    PartTime BOOLEAN NOT NULL,
    Remote BOOLEAN NOT NULL,
    ExpireAt DATE NOT NULL,
    StartedAt DATE NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (EmployerID) REFERENCES Employer (ID)
);

CREATE TABLE ProposalRequirements (
    ID SERIAL PRIMARY KEY,
    ProposalID INT NOT NULL,
    SkillID INT NOT NULL,
    Required BOOLEAN NOT NULL,
    MinAcceptValue INT NOT NULL,
    MinExperience INT DEFAULT 0,
    Priority INT NOT NULL,
    StartedAt DATE NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (ProposalID) REFERENCES Proposal (ID),
    FOREIGN KEY (SkillID) REFERENCES Skill (ID)
);

CREATE TABLE Remuneration (
    ID SERIAL PRIMARY KEY,
    Description VARCHAR(255) NOT NULL,
    Currency VARCHAR(20) NOT NULL,
    Occurrency VARCHAR(20) NOT NULL,
    Type VARCHAR(20) NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL
);

CREATE TABLE ProposalRemuneration (
    ID SERIAL PRIMARY KEY,
    ProposalID INT NOT NULL,
    RemunerationID INT NOT NULL,
    MinValue INT NOT NULL,
    MaxValue INT NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (ProposalID) REFERENCES Proposal (ID),
    FOREIGN KEY (RemunerationID) REFERENCES Remuneration (ID)
);

CREATE TABLE Match (
    ID SERIAL PRIMARY KEY,
    ProposalID INT NOT NULL,
    CandidateID INT NOT NULL,
    CandidateResult BOOLEAN NOT NULL,
    EmployerResult BOOLEAN NOT NULL,
    CandidateReview VARCHAR(255),
    EmployerReview VARCHAR(255),
    Status VARCHAR(20) NOT NULL,
    CreatedAt DATE NOT NULL,
    UpdatedAt DATE NOT NULL,
    Valid BOOLEAN NOT NULL,
    FOREIGN KEY (ProposalID) REFERENCES Proposal (ID),
    FOREIGN KEY (CandidateID) REFERENCES Candidate (ID)
);