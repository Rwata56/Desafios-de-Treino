import io

from desafios_de_treino.paasio import StatsIOWrapper


class TestStatsIOWrapper:
    def test_read_and_write_counts_and_bytes(self):
        buffer = io.BytesIO(b"0123456789")
        wrapper = StatsIOWrapper(buffer)

        # Testar leitura
        data = wrapper.read(4)
        assert data == b"0123"
        assert wrapper.stats.stats() == (1, 0, 4, 0)

        rest = wrapper.read()
        assert rest == b"456789"
        assert wrapper.stats.stats() == (2, 0, 10, 0)

        # Testar escrita
        wrapper.write(b"abc")
        assert wrapper.stats.stats() == (2, 1, 10, 3)

        wrapper.write(b"defgh")
        assert wrapper.stats.stats() == (2, 2, 10, 8)

    def test_context_manager(self):
        buffer = io.BytesIO()
        with StatsIOWrapper(buffer) as wrapped:
            wrapped.write(b"hello")
            result = wrapped.read(
                2
            )  # ler após escrever não retorna nada, mas evita erro
            assert wrapped.stats.read_count == 1
            assert wrapped.stats.write_count == 1
            assert wrapped.stats.read_bytes == 0
            assert wrapped.stats.write_bytes == 5

    def test_zero_length_read_write(self):
        buffer = io.BytesIO()
        wrapper = StatsIOWrapper(buffer)
        wrapper.write(b"")
        wrapper.read(0)
        assert wrapper.stats.stats() == (1, 1, 0, 0)
