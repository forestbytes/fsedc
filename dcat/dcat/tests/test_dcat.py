import pytest
from ..src.dcat import (
    DCATBase,
    DCATMinimum,
    DCATExtended,
)
from pydantic import BaseModel

from dcat_urls import DCAT_URLS

test_urls = DCAT_URLS


class TestDCATBase:
    def test_init(self):
        dcat_base = DCATBase()

        assert dcat_base is not None
        assert isinstance(dcat_base, BaseModel)
        assert isinstance(dcat_base, DCATBase)


class TestDCATMinimum:
    def test_init(self):
        dcat_min = DCATMinimum()

        assert dcat_min is not None
        assert isinstance(dcat_min, BaseModel)
        assert isinstance(dcat_min, DCATBase)
        assert isinstance(dcat_min, DCATMinimum)


class TestDCATExtended:
    def test_init(self):
        dcat_ext = DCATExtended()

        assert dcat_ext is not None
        assert isinstance(dcat_ext, BaseModel)
        assert isinstance(dcat_ext, DCATBase)
        assert isinstance(dcat_ext, DCATExtended)
