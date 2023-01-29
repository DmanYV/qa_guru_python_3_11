import pytest
from selene.support.shared import browser


@pytest.fixture
def desktop_size():
    browser.config.base_url = "https://github.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture
def mobile_size():
    browser.config.base_url = "https://github.com"
    browser.config.window_width = 390
    browser.config.window_height = 844
    yield
    browser.quit()


@pytest.fixture(params=["1920*1080", "390*844"])
def window_size(request):
    if request.param == "1920*1080":
        browser.config.base_url = "https://github.com"
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == "390*844":
        browser.config.base_url = "https://github.com"
        browser.config.window_width = 390
        browser.config.window_height = 844
