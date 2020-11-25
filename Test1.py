import pytest
from automationpractice.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def open_home(app):
    app.open_home_page()
    app.login()
