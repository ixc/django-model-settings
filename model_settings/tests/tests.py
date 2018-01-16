# -*- coding: utf-8 -*-

from __future__ import absolute_import

import datetime
import logging

from django.test import TestCase

from model_settings.models import (SettingValueModel, Boolean,
                                   SettingQuerySet, Integer, SettingModel, Date)
from model_settings.utils import SettingDict

logger = logging.getLogger(__name__)


class TestSettingQuerySet(TestCase):
    def test_as_dict(self):
        settings = SettingQuerySet()
        self.assertTrue(isinstance(settings.as_dict(), dict))

    def test_create(self):
        settings = SettingQuerySet()
        with self.assertRaises(ValueError):
            settings.create("test_name", value=None)
        flag = settings.create("test_name", value=123)
        self.assertIsNotNone(flag)


class TestSettingModel(TestCase):
    def test_get_model_for_value(self):
        with self.assertRaises(ValueError):
            obj = SettingModel.get_model_for_value(type("NonExistent", (), {}))

        obj1 = SettingModel.get_model_for_value(123)
        self.assertEqual(obj1, Integer)

        obj2 = SettingModel.get_model_for_value(datetime.datetime.utcnow())
        self.assertEqual(obj2, Date)


class TestSettingValueModel(TestCase):
    def test_is_compatible(self):
        with self.assertRaises(NotImplementedError):
            SettingValueModel.is_compatible(None)


class TestBooleanType(TestCase):
    def test_value_type(self):
        check = lambda x, y: True if x is y else False
        boolean_type = Boolean()
        flag_value_type = check(boolean_type.value_type, bool)
        self.assertTrue(flag_value_type)


class TestSettingsDict(TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            obj = SettingDict()
