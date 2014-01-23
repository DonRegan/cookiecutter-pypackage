
# Copyright (C) {{ cookiecutter.year }} {{ cookiecutter.credits }}

"""
Tests for `{{ cookiecutter.repo_name }}` module.
"""
import pytest
from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}


class Test{{ cookiecutter.repo_name|capitalize }}(object):

    def setup(self):
        pass

    def test_something(self):
        x = 1
        assert x==1

    def teardown(self):
        pass
