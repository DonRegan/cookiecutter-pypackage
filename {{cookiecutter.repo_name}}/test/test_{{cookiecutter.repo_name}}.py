# {{ cookiecutter.repo_name }} is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# {{ cookiecutter.repo_name }} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with {{ cookiecutter.repo_name }}.  If not, see <http://www.gnu.org/licenses/>.


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