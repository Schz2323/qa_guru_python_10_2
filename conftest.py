import pytest
@pytest.fixture(scope="module")
def browser():
    print("Браузер")

    yield

    print("Закрываем браузер")
