from dataclasses import dataclass
from typing import Callable, List

from django.http import HttpRequest
from django.db.models import Exists, QuerySet
from django import forms
from django.contrib.auth.models import User

from allianceauth.eveonline.models import EveCharacter
from esi.models import Token


@dataclass
class LoginImport:
    app_label: str
    unique_id: str
    field_label: str
    add_character: Callable[[HttpRequest, Token], None]
    scopes: List[str]
    check_permissions: Callable[[User], bool]
    is_character_added: Callable[[EveCharacter], bool]
    is_character_added_annotation: Exists
    get_users_with_perms: Callable[[], QuerySet[User]]

    def get_query_id(self):
        return f"{self.app_label}_{self.unique_id}"

    def __hash__(self) -> int:
        return hash(self.get_query_id())


@dataclass
class AppImport:
    app_label: str
    imports: List[LoginImport]

    def get_form_fields(self, user):
        return {
            import_.get_query_id(): forms.BooleanField(
                required=False,
                initial=True,
                label=import_.field_label
            )
            for import_ in self.imports
            if import_.check_permissions(user)
        }

    def get_imports_with_perms(self, user: User):
        return AppImport(
            self.app_label,
            [
                import_
                for import_ in self.imports
                if import_.check_permissions(user)
            ]
        )

    def has_any_perms(self, user: User):
        return any(import_.check_permissions(user) for import_ in self.imports)

    def get(self, unique_id: str) -> LoginImport:
        for import_ in self.imports:
            if import_.unique_id == unique_id:
                return import_

        raise KeyError(f"Import with unique_id {unique_id} not found")
