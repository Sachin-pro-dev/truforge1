"""Split a sequence into fixed-size, 1-indexed pages."""

from typing import Sequence, TypeVar

T = TypeVar("T")


class PageOutOfRange(IndexError):
    """Raised when a requested page number does not exist."""


def _validate(page: int, per_page: int) -> None:
    if not isinstance(per_page, int) or per_page < 1:
        raise ValueError(f"per_page must be a positive integer, got {per_page!r}")
    if not isinstance(page, int) or page < 1:
        raise ValueError(f"page must be a positive integer, got {page!r}")


def page_count(total: int, per_page: int) -> int:
    """Return how many pages are needed to show `total` items."""
    if total < 0:
        raise ValueError(f"total must be non-negative, got {total!r}")
    _validate(1, per_page)
    return (total + per_page - 1) // per_page


def paginate(items: Sequence[T], page: int, per_page: int) -> list[T]:
    """Return the items on `page` (1-indexed)."""
    _validate(page, per_page)
    if page > page_count(len(items), per_page):
        raise PageOutOfRange(f"page {page} does not exist")
    start = (page - 1) * per_page
    return list(items[start : start + per_page])


def has_next(total: int, page: int, per_page: int) -> bool:
    """Return True if there is a page after `page`."""
    _validate(page, per_page)
    return page < page_count(total, per_page)
