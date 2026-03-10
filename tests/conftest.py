import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def clean_activities():
    baseline = copy.deepcopy(activities)

    yield

    activities.clear()
    activities.update(baseline)


@pytest.fixture
def client(clean_activities):
    return TestClient(app)
