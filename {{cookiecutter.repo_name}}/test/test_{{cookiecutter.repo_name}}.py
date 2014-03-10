
# Copyright (C) {{ cookiecutter.year }} {{ cookiecutter.credits }}

"""
Tests for `{{ cookiecutter.repo_name }}` module.
"""
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest
from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}


class Test{{ cookiecutter.repo_name|capitalize }}(object):

    def setup(self):
        #prepare unit test. Load data etc
        print("setting up " + __name__)
        pass

    def test_something(self):
        x = 1
        assert x==1

    def teardown(self):
        #tidy up
        print("tearing down " + __name__)
        pass

if __name__ == '__main__':
    pytest.main()