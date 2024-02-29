""" unit tests for aedev_pythonanywhere module package.

minimal testing because of the rate-limits on pythonanywhere.com (each endpoint has a 40 requests per minute rate limit,
apart from the send_input endpoint on consoles, which is 120 requests per minute - see
`https://help.pythonanywhere.com/pages/API`__ for more details).
"""
import os
import pytest
import requests

from conftest import skip_gitlab_ci
from unittest.mock import Mock, patch

from ae.base import PY_CACHE_FOLDER, PY_INIT, norm_name
from aedev.pythonanywhere import SKIP_ROOT_FOLDERS, PythonanywhereApi


TEST_PACKAGE_NAME = 'aedev_pythonanywhere_tests'    #: package name used for integrity tests on web server
path_pkg3 = 'test2/sub2'
file_pkg3 = f'{path_pkg3}/file_pkg3.z'
migration_pkg3 = f'{path_pkg3}/' + 'migrations' + '/mig_fil.wxy'
one_pkg_paths = {file_pkg3, f'{path_pkg3}/{PY_INIT}'}
all_pkg_paths = one_pkg_paths | {'test1/namespace_mod.py'}
skipped_web_paths = {f'{PY_CACHE_FOLDER}/x.y', f'test1/{PY_CACHE_FOLDER}/y.Z',
                     migration_pkg3,
                     'static' + '/static_file.ttt', 'media' + '/media_file.jjj', 'media_ini' + '/med.ia',
                     TEST_PACKAGE_NAME + '/' + 'static' + '/baseball.html'}
skipped_lean_paths = {'not_deployed_root_file.xxx',
                      'db.sqlite', 'project.db',
                      'manage.py',
                      'test1/fi1.po'}

def _prepare_host_files(connection):
    del_fil = 'test0/sub4/del_file.txt'
    assert not connection.deploy_file(del_fil, b"deleted to test empty root folder")
    assert connection.error_message == ""
    assert not connection.delete_file_or_folder(del_fil)
    assert connection.error_message == ""
    for fil_pat in all_pkg_paths | skipped_web_paths | skipped_lean_paths:
        assert not connection.deploy_file(fil_pat, b"content of " + fil_pat.encode())
        assert connection.error_message == ""


@pytest.fixture
def connection():
    """ provide personal pythonanywhere remote web server for tests only running locally with personal credentials. """
    web_domain = "www.pythonanywhere.com"
    web_user = "AndiEcker"
    from dotenv import load_dotenv
    load_dotenv()
    web_token = os.environ.get(f'AE_OPTIONS_WEB_TOKEN_AT_{norm_name(web_domain).upper()}')

    remote_connection = PythonanywhereApi(web_domain, web_user, web_token, TEST_PACKAGE_NAME)

    yield remote_connection


def test_pythonanywhere_declarations():
    """ test the module declarations (also for having at least one test case running on gitlab ci). """
    assert PythonanywhereApi
    assert SKIP_ROOT_FOLDERS
    assert isinstance(SKIP_ROOT_FOLDERS, tuple)

    assert norm_name(TEST_PACKAGE_NAME) == TEST_PACKAGE_NAME

    assert requests             # not-used-inspection-warning workaround, used for requests.Response.json() patching


@skip_gitlab_ci  # skip on gitlab because of missing remote repository user account token
class TestLocallyOnly:
    def test_available_consoles(self, connection):
        consoles = connection.available_consoles()
        assert isinstance(consoles, list)

    def test_deploy_file(self, connection):
        assert connection.error_message == ""

        connection.delete_file_or_folder("")  # if last test run failed then wipe folder TEST_PACKAGE_NAME on host

        file_path = os.path.join(TEST_PACKAGE_NAME, PY_INIT)
        dep_version = '3.6.9'
        file_content = f'""" test package doc string. """\n\n__version__ = \'{dep_version}\'\n'.encode()

        assert not connection.deploy_file(file_path, file_content)
        assert connection.error_message == ""

        assert connection.deployed_code_files() == {file_path}
        assert connection.error_message == ""

        assert connection.deployed_file_content(file_path) == file_content
        assert connection.error_message == ""

        inv_fil_path = "any/not/existing/file_path"
        assert connection.deployed_file_content(inv_fil_path) is None
        assert inv_fil_path in connection.error_message

        assert connection.deployed_version() == dep_version
        assert connection.error_message == ""

        assert not connection.delete_file_or_folder(file_path)      # delete test file
        assert connection.error_message == ""
        assert not connection.delete_file_or_folder("")             # also delete test folder TEST_PACKAGE_NAME
        assert connection.error_message == ""

    def test_find_package_files(self, connection):
        connection.delete_file_or_folder("")  # if last test run failed then wipe folder TEST_PACKAGE_NAME on host
        _prepare_host_files(connection)

        assert connection.find_package_files("not_existing_file_name") is None   # test error
        assert connection.error_message
        assert isinstance(connection.error_message, str)

        tst_err_msg = "test error message"
        def _raise_json_err(_content_to_json):
            raise Exception(tst_err_msg)
        with patch('requests.Response.json', new=_raise_json_err):
            assert connection.find_package_files() is None  # simulate broken response.content for coverage
            assert tst_err_msg in connection.error_message

        # coverage: patch requests.api.request to patch requests.get, which is not patchable because it is set to the
        # method parameter of PythonanywhereApi._request(), to test error propagation from recursive
        # find_package_files() calls
        tst_err_msg = "tst err message"
        def _raise_requests_get_err(*_args, **_kwargs):
            if path_pkg3 in _args[1]:               # _args[1] contains first requests.get argument (url)
                return Mock()                   # simulate error response
            else:
                return requests.request(*_args, **_kwargs)
        # with patch('requests.request', ) doesn't work
        # even patch('aedev.pythonanywhere.requests.api.get', ) doesn't work
        with patch('requests.api.request', new=_raise_requests_get_err):
            assert connection.find_package_files() is None  # error from deeper recursion level get propagated
            assert path_pkg3 in connection.error_message

        found_paths = connection.find_package_files()
        assert connection.error_message == ""
        assert found_paths == all_pkg_paths | skipped_web_paths | skipped_lean_paths

        found_paths = connection.find_package_files(skip_file_path=lambda _: "_pkg3" not in _)
        assert connection.error_message == ""
        assert found_paths == {file_pkg3}

        found_paths = connection.find_package_files("test2")
        assert connection.error_message == ""
        assert found_paths == one_pkg_paths | {migration_pkg3}

        assert not connection.delete_file_or_folder("test1")     # delete test1 folder with content
        assert connection.error_message == ""
        assert not connection.delete_file_or_folder("")          # finally delete test root folder TEST_PACKAGE_NAME
        assert connection.error_message == ""


class TestPythonAnywhereWithoutConnection:
    def test_web_file_exclude(self):
        instance = PythonanywhereApi("any domain", "any user", "any token", TEST_PACKAGE_NAME)

        for file_path in all_pkg_paths | skipped_lean_paths:
            assert not instance.web_file_exclude(file_path)

        for file_path in all_pkg_paths:
            assert not instance.web_lean_file_exclude(file_path)

        assert instance.web_file_exclude(os.path.join('migrations', "any filename"))
        assert instance.web_file_exclude(os.path.join('root_folder', 'migrations', "any filename"))

        for folder in SKIP_ROOT_FOLDERS:
            assert instance.web_file_exclude(os.path.join(folder, "any filename"))
            assert not instance.web_file_exclude(os.path.join("any root folder", folder))
            assert not instance.web_file_exclude(os.path.join("any root folder", folder, "any filename"))
