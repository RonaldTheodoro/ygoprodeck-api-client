import pathlib


class Settings:
    base_dir = pathlib.Path(__file__).parent

    @property
    def test_resources(self):
        return self.base_dir / 'tests/resources'

    @property
    def cassettes_dir(self):
        return self.test_resources / 'cassettes'

    @property
    def test_payloads(self):
        return self.test_resources / 'payloads'


settings = Settings()
