from typing import ClassVar


class LargestSeriesProduct:
    series: str
    span: int

    def __init__(self, series: str, span: int) -> None:
        self.series = series
        self.span = span

    def largest_product(self) -> int:
        if self.span < 0:
            raise ValueError("span must not be negative")
        if self.span > len(self.series):
            raise ValueError("span must be smaller than string length")
        if any(not ch.isdigit() for ch in self.series):
            raise ValueError("digits input must only contain digits")
        if self.span == 0:
            return 1

        max_product: int = 0
        for i in range(len(self.series) - self.span + 1):
            chunk = self.series[i : i + self.span]
            product = 1
            for ch in chunk:
                product *= int(ch)
            if product > max_product:
                max_product = product

        return max_product
