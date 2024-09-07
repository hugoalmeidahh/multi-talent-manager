from ninja import Schema

class CandidateSchema(Schema):
    id: int
    name: str
    email: str
    status: str
    skills: str

class CandidateCreateSchema(Schema):
    name: str
    email: str
    status: str
    skills: str
