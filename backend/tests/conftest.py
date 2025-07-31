import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """Create all tables before tests and clean up after."""
    # Only run if we're in testing mode
    if os.getenv("TESTING"):
        try:
            from app.database import Base, engine  # type: ignore

            # Create all tables before the tests
            Base.metadata.create_all(bind=engine)
            yield
            # Remove all tables after the tests
            Base.metadata.drop_all(bind=engine)
        except ImportError:
            # Skip if app.database is not available
            yield
    else:
        yield
