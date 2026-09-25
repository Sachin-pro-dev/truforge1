"""Build the paginated response bodies returned by the listing endpoints."""

from typing import Any, Sequence

from .pagination import has_next, page_count, paginate


def page_response(items: Sequence[Any], page: int, per_page: int) -> dict[str, Any]:
    """Return a JSON-ready dict describing one page of `items`."""
    total = len(items)
    return {
        "items": paginate(items, page, per_page),
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": page_count(total, per_page),
        "has_next": has_next(total, page, per_page),
    }
