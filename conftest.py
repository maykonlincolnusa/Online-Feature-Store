"""
Pytest configuration and fixtures
"""

import pytest
import redis
from datetime import datetime
from typing import Generator
import pandas as pd


@pytest.fixture(scope="session")
def redis_client() -> Generator:
    """Fixture para cliente Redis de teste"""
    client = redis.Redis(
        host='localhost',
        port=6379,
        db=15,  # Use DB separada para testes
        decode_responses=True
    )
    
    yield client
    
    # Cleanup
    client.flushdb()
    client.close()


@pytest.fixture
def sample_user_data() -> pd.DataFrame:
    """Fixture com dados de usuário de exemplo"""
    return pd.DataFrame([
        {
            "user_id": "user_1",
            "birth_date": datetime(1990, 1, 1),
            "subscription_type": "premium",
            "transaction_timestamp": datetime(2024, 1, 15, 10, 30),
            "transaction_amount": 100.0,
            "user_avg_purchase_value": 80.0
        },
        {
            "user_id": "user_2",
            "birth_date": datetime(1985, 6, 15),
            "subscription_type": "basic",
            "transaction_timestamp": datetime(2024, 1, 15, 14, 20),
            "transaction_amount": 50.0,
            "user_avg_purchase_value": 60.0
        }
    ])


@pytest.fixture
def sample_event() -> dict:
    """Fixture com evento de exemplo"""
    return {
        "user_id": "user_123",
        "birth_date": datetime(1990, 5, 15),
        "transaction_timestamp": datetime.now(),
        "transaction_amount": 150.0,
        "user_avg_purchase_value": 100.0,
        "subscription_type": "premium"
    }