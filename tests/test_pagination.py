import pytest

from pagekit import PageOutOfRange, has_next, page_response, paginate


ITEMS = list(range(10))


def test_first_page():
    assert paginate(ITEMS, 1, 3) == [0, 1, 2]


def test_middle_page():
    assert paginate(ITEMS, 2, 3) == [3, 4, 5]


def test_works_on_tuples_and_strings():
    assert paginate(tuple("abcdefg"), 2, 2) == ["c", "d"]
    assert paginate("abcdefg", 1, 4) == ["a", "b", "c", "d"]


def test_page_far_past_the_end_raises():
    with pytest.raises(PageOutOfRange):
        paginate(ITEMS, 10, 3)


@pytest.mark.parametrize("page", [0, -1])
def test_page_must_be_positive(page):
    with pytest.raises(ValueError):
        paginate(ITEMS, page, 3)


@pytest.mark.parametrize("per_page", [0, -5, 2.5])
def test_per_page_must_be_positive_int(per_page):
    with pytest.raises(ValueError):
        paginate(ITEMS, 1, per_page)


def test_has_next_on_first_page():
    assert has_next(len(ITEMS), 1, 3) is True


def test_page_response_shape():
    body = page_response(ITEMS, 1, 3)
    assert body["items"] == [0, 1, 2]
    assert body["page"] == 1
    assert body["per_page"] == 3
    assert body["total"] == 10
    assert body["has_next"] is True
