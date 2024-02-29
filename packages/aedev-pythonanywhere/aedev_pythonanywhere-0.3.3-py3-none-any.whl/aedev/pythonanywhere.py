""" web api for www.pyanywhere.com and eu.pyanywhere.com

"""
import os
import requests

from typing import Any, Callable, Optional, Sequence, Union, cast

from ae.base import DOCS_FOLDER, PY_CACHE_FOLDER, PY_INIT, TESTS_FOLDER                 # type: ignore
from aedev.setup_project import code_version                                            # type: ignore


__version__ = '0.3.3'


SKIP_ROOT_FOLDERS = (DOCS_FOLDER, '.git', '.idea', 'media', 'media_ini', 'static', TESTS_FOLDER)
""" root folders on the web server that will skipped on search of deployed project package files. """


class PythonanywhereApi:
    """ remote host api to a project package on the web hosts eu.pythonanywhere.com and pythonanywhere.com. """

    def __init__(self, web_domain: str, web_user: str, web_token: str, package_name: str):
        """ initialize web host api and the deployed project package name.

        :param web_domain:      remote web host domain.
        :param web_user:        remote connection username.
        :param web_token:       personal user credential token string on remote host.
        :param package_name:    name of the web project package.
        """
        self.error_message = ""

        self.base_url = f"https://{web_domain}/api/v0/user/{web_user}/"
        self.consoles_url_part = "consoles/"
        self.protocol_headers = {'Authorization': f"Token {web_token}"}

        # self.web_domain = web_domain
        self.web_user = web_user
        # self.web_token = web_token
        self.package_name = self._package_name = package_name

    @property
    def package_name(self) -> str:
        """ package name string property:

        :getter:                return the currently connected/configured package name of the web host server.
        :setter:                set/change the currently connected/configured package name of the web host server.
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name: str):
        self.files_url_part = f"files/path/home/{self.web_user}/{package_name}/"
        self._package_name = package_name

    def _from_json(self, response: requests.Response) -> Optional[Union[list[dict[str, Any]], dict[str, Any]]]:
        """ convert json in response to python type (list/dict).

        :param response:        response from requests to convert into python data type.
        :return:                [list of] dictionaries converted from the response content or None on error.
        """
        try:
            return response.json()
        except Exception as exc:  # requests.exceptions.JSONDecodeError
            self.error_message = f"{exc} in response.json() call on response content '{response.content!r}'"
            return None

    def _request(self, url_path: str, task: str, method: Callable = requests.get, success_codes: Sequence = (200, 201),
                 **request_kwargs) -> requests.Response:
        """ send a https request specified via :paramref:`.method` and return the response.

        :param url_path:        sub url path to send request to.
        :param task:            string describing the task to archive (used to compile an error message).
        :param method:          requests method (get, post, push, delete, patch, ...).
        :param success_codes:   sequence of response.status_code success codes
        :param request_kwargs:  additional request method arguments.
        :return:                request response. the :attr:`.error_message` will be set on error, else reset to "".
        """
        response = method(f"{self.base_url}{url_path}", headers=self.protocol_headers, **request_kwargs)
        if response.status_code in success_codes:
            self.error_message = ""
        else:
            self.error_message = (f"request error '{response.status_code}:{response.reason}'"
                                  f" {task} via '{self.base_url}{url_path}'")
        return response

    def available_consoles(self) -> Optional[list[dict[str, Any]]]:
        """ determine the available consoles.

        :return:                python dictionary with available consoles or None if an error occurred.
        """
        response = self._request(self.consoles_url_part, "get list of consoles")
        if self.error_message:
            return None
        return cast(Optional[list[dict[str, Any]]], self._from_json(response))

    def deployed_code_files(self, lean: bool = False) -> Optional[set[str]]:
        """ determine all deployed code files of given package name deployed to the pythonanywhere server.

        :param lean:            pass True to additionally exclude repository files that are not needed on the web
                                production server like e.g. the gettext '.po' files, the 'media_ini' root folder,
                                and the 'static' sub-folder with the initial static files of the web project.
        :return:                set of file paths of the package deployed on the web, relative to the project root
                                or None if an error occurred.
        """
        return self.find_package_files(skip_file_path=self.web_lean_file_exclude if lean else self.web_file_exclude)

    def deployed_file_content(self, file_path: str) -> Optional[bytes]:
        """ determine the file content of a file deployed to a web server.

        :param file_path:       path of a deployed file relative to the project root.
        :return:                file content as bytes or None if error occurred (check self.error_message).
        """
        response = self._request(self.files_url_part + file_path, "fetching file content")
        if self.error_message:
            return None
        return response.content

    def deployed_version(self) -> str:
        """ determine the version of a deployed django project package.

        :return:                version string of the package deployed to the web host/server
                                or empty string if package version file or version-in-file not found.
        """
        init_file_content = self.deployed_file_content(os.path.join(self.package_name, PY_INIT))
        return "" if init_file_content is None else code_version(init_file_content)

    def deploy_file(self, file_path: str, file_content: bytes) -> str:
        """ add or update a project file to the web server.

        :param file_path:       path relative to the project root of the file to be deployed (added or updated).
        :param file_content:    file content to deploy/upload.
        :return:                error message if update/add failed else on success an empty string.
        """
        self._request(self.files_url_part + file_path, f"deploy file {file_path}", method=requests.post,
                      files={'content': file_content})
        return self.error_message

    def delete_file_or_folder(self, file_path: str) -> str:
        """ delete a file or folder on the web server.

        :param file_path:       path relative to the project root of the file to be deleted.
        :return:                error message if deletion failed else on success an empty string.
        """
        self._request(self.files_url_part + file_path, f"deleting file {file_path}", method=requests.delete,
                      success_codes=(204, ))
        return self.error_message

    def find_package_files(self, file_path: str = "", skip_file_path: Callable[[str], bool] = lambda _: False
                           ) -> Optional[set[str]]:
        """ determine the package files deployed onto the app/web server.

        not using the files tree api endpoints/function (f"files/tree/?path=/home/{self.web_user}/{package_name}")
        because their response is limited to 1000 files
        (see https://help.pythonanywhere.com/pages/API#apiv0userusernamefilestreepathpath) and e.g. kairos has more
        than 5300 files in its package folder (mainly for django filer and the static files).

        :param file_path:       folder path relative to the project root to be searched (not ending with a slash).
        :param skip_file_path:  called for each found file with the file_path relative to the package root folder
                                as argument, returning True to exclude the specified file from the returned result set.
                                you may use :meth:`.web_file_exclude` and :meth:`.web_lean_file_exclude` or an extended
                                callable from these two methods.
        :return:                set of file paths of the package deployed on the web, relative to the project root
                                or None if an error occurred. all files underneath a
        """
        url_path = self.files_url_part
        if file_path:
            url_path += file_path + '/'
        response = self._request(url_path, f"fetching files in folder {file_path}")
        if self.error_message:
            return None

        folder_dict = self._from_json(response)
        if folder_dict is None:
            return None

        folder_files = set()
        for entry, attr in folder_dict.items():                         # type: ignore
            found_file_path = os.path.join(file_path, entry)
            if attr['type'] == 'directory':
                sub_dir_files = self.find_package_files(file_path=found_file_path, skip_file_path=skip_file_path)
                if sub_dir_files is None:
                    return None
                folder_files.update(sub_dir_files)
            elif not skip_file_path(found_file_path):
                folder_files.add(found_file_path)

        return folder_files

    def web_file_exclude(self, file_path: str) -> bool:
        """ default file exclude callback used by `meth:`.deployed_code_files` to call :meth:`.find_package_files`.

        :param file_path:       path to file to check for exclusion, relative to the project root folder.
        :return:                True if the file specified in :paramref:`.rel_file_path` has to excluded, else False.
        """
        parts = file_path.split('/')
        return (
                PY_CACHE_FOLDER in parts
                or 'migrations' in parts
                or parts[0] in SKIP_ROOT_FOLDERS
                or parts[0] == self.package_name and parts[1] == 'static'
                )

    def web_lean_file_exclude(self, file_path: str) -> bool:
        """ lean file exclude callback used by `meth:`.deployed_code_files` to call :meth:`.find_package_files`.

        :param file_path:       path to file to check for exclusion, relative to the project root folder.
        :return:                True if the file specified in :paramref:`.rel_file_path` has to excluded, else False.
        """
        return (self.web_file_exclude(file_path)
                or os.path.splitext(file_path)[1] == '.po'
                or '/' not in file_path and ('db' in file_path.split('.')        # 'db.sqlite', 'project.db', ...
                                             or file_path != 'manage.py')
                )
