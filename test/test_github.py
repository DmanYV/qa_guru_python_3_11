import pytest
from selene.support.shared import browser
from selene import have


def test_github_open_in_desktop(desktop_size):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_open_in_mobile(mobile_size):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("window_size", ["1920*1080"], indirect=True)
def test_github_desktop_from_mark(window_size):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("window_size", ["390*844"], indirect=True)
def test_github_mobile_from_mark(window_size):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("window_width,window_height",
                         [pytest.param(1920, 1080),
                          pytest.param(390, 844)
                          ])
def test_github_desktop(window_width, window_height):
    if window_width == 390:
        pytest.skip(reason='Пропускаем мобильную версию в данном тесте')
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("window_width,window_height",
                         [pytest.param(1920, 1080, id="desktop version"),
                          pytest.param(390, 844, id="mobile_version")
                          ])
def test_github_mobile(window_width, window_height):
    if window_width == 1920:
        pytest.skip(reason='Пропускаем десктопную версию в данном тесте')
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
