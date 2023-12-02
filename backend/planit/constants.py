from enum import Enum


class Environment(str, Enum):
    LOCAL = "LOCAL"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self):
        return self in (self.LOCAL, self.TESTING)

    @property
    def is_testing(self):
        return self == self.TESTING

    @property
    def is_deployed(self) -> bool:
        return self == self.PRODUCTION
