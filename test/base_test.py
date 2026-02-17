import pytest
from utilities.logger import get_logger


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request, driver, config):

        request.cls.driver = driver
        request.cls.config = config["environments"]["practice"]

        self.logger = get_logger(self.__class__.__name__)
        self.logger.info("ShoppersStack Test Started")
        yield
        self.logger.info("ShoppersStack Test Ended")