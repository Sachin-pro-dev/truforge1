from pagekit import page_response, paginate


def test_incomplete_final_page_is_reachable_and_advertised():
    invoices = list(range(10))

    has_next_from_page_three = page_response(invoices, 3, 3)["has_next"]
    try:
        page_four_items = paginate(invoices, 4, 3)
    except Exception as exc:  # pragma: no cover - assertion below reports the public symptom
        page_four_items = type(exc).__name__

    assert (has_next_from_page_three, page_four_items) == (True, [9])
