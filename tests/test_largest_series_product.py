from desafios_de_treino.largest_series_product import LargestSeriesProduct


def test_basic_largest_product():
    lsp = LargestSeriesProduct("1234", 2)
    assert lsp.largest_product() == 12  # 3 × 4


def test_largest_product_with_zero_span():
    lsp = LargestSeriesProduct("", 0)
    assert lsp.largest_product() == 1


def test_large_series_example():
    series = "1027839564"
    lsp = LargestSeriesProduct(series, 3)
    assert lsp.largest_product() == 270  # 9 × 5 × 6


def test_span_negative_raises():
    lsp = LargestSeriesProduct("123", -1)
    try:
        lsp.largest_product()
    except ValueError as e:
        assert str(e) == "span must not be negative"


def test_span_too_large_raises():
    lsp = LargestSeriesProduct("123", 5)
    try:
        lsp.largest_product()
    except ValueError as e:
        assert str(e) == "span must be smaller than string length"


def test_non_digit_characters_raise():
    lsp = LargestSeriesProduct("12a3", 2)
    try:
        lsp.largest_product()
    except ValueError as e:
        assert str(e) == "digits input must only contain digits"
