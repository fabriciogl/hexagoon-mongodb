#  Copyright (c) 2022. Hexagoon. Criador: Fabricio Gatto Lourençone. Todos os direitos reservados.
import datetime
from typing import Optional, List, Union, Any

from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field

from api.v1.role.model.role_model import RoleUsuarioTokenOut, RolePrecedenciaIn


class UsuarioIn(BaseModel):
    id: Optional[Union[str, ObjectId]] = Field(None, alias='_id')
    nome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    ativo: Optional[bool]

    class Config:
        title = 'usuarios'
        arbitrary_types_allowed = True


class UsuarioOut(BaseModel):
    id: Optional[Union[str, Any]] = Field(None, alias='_id')
    nome: Optional[str]
    email: Optional[EmailStr]
    ativo: Optional[str]
    roles: Optional[List[RoleUsuarioTokenOut]]

    class Config:
        title = 'usuarios'


class UsuarioOutReduzido(BaseModel):
    id: int
    nome: str
    email: EmailStr


class Usuario(BaseModel):
    id: Optional[Union[str, ObjectId]] = Field(None, alias='_id')
    nome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    ativo: Optional[bool]
    roles: Optional[list[RolePrecedenciaIn]]

    # accountability
    criado_em: Optional[datetime.datetime]
    criado_por: Optional[ObjectId]
    alterado_em: Optional[datetime.datetime]
    alterado_por: Optional[ObjectId]
    # softdelete
    deletado_em: Optional[datetime.datetime]
    deletado_por: Optional[ObjectId]

    class Config:
        title = 'usuarios'
        arbitrary_types_allowed = True


class UsuarioTokenIn(BaseModel):
    email: Optional[EmailStr]
    senha: Optional[str]

    class Config:
        title = 'usuarios'


class UsuarioTokenOut(BaseModel):
    id: Optional[Union[str, Any]] = Field(None, alias='_id')
    email: Optional[EmailStr]
    senha: Optional[str]
    rolePrecedencias: Optional[list]

    class Config:
        title = 'usuarios'