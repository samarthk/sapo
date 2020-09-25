import pytest
import os

from sapo.schema_fetcher import *
from sapo.parquet_validator import ParquetValidator


dirname = os.path.dirname(__file__)


def test_yaml_to_pyarrow_schema():
    filename = os.path.join(dirname, './schemas/players_pyarrow_schema.yml')
    expected_schema = pa.schema([
        pa.field("id", pa.int64(), True),
        pa.field("last_name", pa.string(), True),
        pa.field("position", pa.string(), True)])
    assert yaml_to_pyarrow_schema(filename) == expected_schema


def test_validate_schema():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './data/players.parquet')
    p = ParquetValidator(filename)

    filename = os.path.join(dirname, './schemas/players_pyarrow_schema.yml')
    expected_schema = yaml_to_pyarrow_schema(filename)

    assert p.validate_schema(expected_schema) == True
