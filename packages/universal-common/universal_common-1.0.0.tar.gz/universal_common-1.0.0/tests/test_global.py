from universal_common import coalesce

class TestGlobal:
    def test_coalesce_works(self):
        assert coalesce() is None
        assert coalesce(None, 1) == 1
        assert coalesce(2, 1) == 2
        assert coalesce(3) == 3
        assert coalesce(4, None) == 4