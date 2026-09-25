# pagekit

Tiny helpers for paginating lists in API responses.

```python
from pagekit import paginate, page_response

paginate(list(range(10)), page=2, per_page=3)   # [3, 4, 5]
page_response(users, page=1, per_page=20)       # {"items": [...], "total_pages": ..., "has_next": ...}
```

Pages are 1-indexed. Requesting a page that does not exist raises `PageOutOfRange`.

## Development

```bash
pip install -e ".[dev]"
pytest
```
