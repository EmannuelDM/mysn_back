from typing import Optional
from fastapi_filter.contrib.sqlalchemy import Filter
from users.models import DbUser


class UserFilter(Filter):
    class Constants(Filter.Constants):
        model = DbUser
        search_field_name = "search"
        search_model_fields = ["name", "email"]

    order_by: Optional[list[str]] = None
    search: Optional[str] = None  # It will search in both `name` and `email` columns.
