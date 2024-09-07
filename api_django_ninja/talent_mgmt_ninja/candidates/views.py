import jwt
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.conf import settings
from ninja import Router
from ninja.errors import HttpError
from ninja.pagination import paginate
from ninja.security import django_auth
from typing import List

from candidates.models import Candidate
from candidates.schemas import CandidateSchema, CandidateCreateSchema
from talent_mgmt_ninja.auth import JWTAuth

router = Router()

@router.post("/token/")
def login(request, username: str, password: str):
    user = authenticate(username=username, password=password)
    if not user:
        raise HttpError(401, "Invalid credentials")

    # Gerar o token JWT
    payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + settings.JWT_SETTINGS['ACCESS_TOKEN_LIFETIME']
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_SETTINGS['ALGORITHM'])
    return {"token": token}

@router.get("/candidates/", response=List[CandidateSchema], auth=JWTAuth())
@paginate()
def list_candidates(request, status: str = None, search: str = None):
    queryset = Candidate.objects.all()
    if status:
        queryset = queryset.filter(status=status)
    if search:
        queryset = queryset.filter(skills__icontains=search)
    return queryset

@router.post("/candidates/", response=CandidateSchema, auth=JWTAuth())
def create_candidate(request, data: CandidateCreateSchema):
    candidate = Candidate.objects.create(**data.dict())
    return candidate

@router.get("/candidates/{id}/", response=CandidateSchema, auth=JWTAuth())
def get_candidate(request, id: int):
    candidate = get_object_or_404(Candidate, id=id)
    return candidate

@router.put("/candidates/{id}/", response=CandidateSchema, auth=JWTAuth())
def update_candidate(request, id: int, data: CandidateCreateSchema):
    candidate = get_object_or_404(Candidate, id=id)
    for attr, value in data.dict().items():
        setattr(candidate, attr, value)
    candidate.save()
    return candidate

@router.delete("/candidates/{id}/", auth=JWTAuth())
def delete_candidate(request, id: int):
    if not request.auth.is_staff:
        return {"error": "Unauthorized"}, 403
    candidate = get_object_or_404(Candidate, id=id)
    candidate.delete()
    return {"success": True}
