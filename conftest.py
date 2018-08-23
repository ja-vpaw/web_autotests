from fixture.application import Application
import pytest

fixture = None

@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        print("Fixture is None")
        fixture = Application()
    else:
        if not fixture.is_valid():
            print("Fixture is not valid")
            fixture = Application()
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
