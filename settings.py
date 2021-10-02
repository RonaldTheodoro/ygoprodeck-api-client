import pathlib


class Settings:
    base_dir = pathlib.Path(__file__).parent

    @property
    def cassettes_dir(self):
        return self.base_dir / 'tests/resources/cassettes'


settings = Settings()
