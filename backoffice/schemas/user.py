from typing import List, Optional
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from backoffice.schemas.email import Email, EmailField, EmailOut
from backoffice.schemas.phone import Phone, PhoneField, PhoneOut


class UserStatusOut(SQLModel):
	slug: str = Field(max_length=64)


class UserStatus(UserStatusOut, table=True):
	__tablename__ = "users_status"
	id_user_status: int = Field(primary_key=True)
	user: List["User"] = Relationship(back_populates="status")


class UserPasswordField(SQLModel):
	password: str = Field(max_length=64)


class UserBase(SQLModel):
    first_name: str = Field(max_length=64)
    last_name: str = Field(max_length=64)


class User(UserBase, UserPasswordField, table=True):
	__tablename__ = "users"
	id_user: Optional[int] = Field(primary_key=True)
	id_user_status: int = Field(foreign_key="users_status.id_user_status")

	status: UserStatus = Relationship(back_populates="user")
	email: Email = Relationship(back_populates="user", sa_relationship_kwargs={'uselist': False})
	phone: Phone = Relationship(back_populates="user", sa_relationship_kwargs={'uselist': False})


class UserCreate(UserBase, UserPasswordField, EmailField, PhoneField):
	pass


class UserLoginByEmail(EmailField, UserPasswordField):
	pass


class UserInformation(UserBase):
	status: UserStatusOut
	email: EmailOut
	phone: PhoneOut