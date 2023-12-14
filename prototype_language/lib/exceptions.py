import traceback
from lib.constants import PrototypeLanguageJobs


class PrototypeLanguageJob:
    class JobNotExists(Exception):
        def __init__(self, message: str):
            self.jobs = PrototypeLanguageJobs.__ALL_JOBS__
            # Add jogs into message.
            message += f"\n{self.jobs}"
            super().__init__(message)
            self.traceback = traceback.format_exc()

class System:
    class Arguments(Exception):
        def __init__(self, message: str):
            super().__init__(message)
            self.traceback = traceback.format_exc()