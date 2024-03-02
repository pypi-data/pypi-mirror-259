#########################################################################
#                                                                       #
#  This file is part of gazix.                                          #
#                                                                       #
#  gazix is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by #
#  the Free Software Foundation, either version 3 of the License, or    #
#  (at your option) any later version.                                  #
#                                                                       #
#  gazix is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of       #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        # 
#  GNU General Public License for more details.                         #
#                                                                       #
#  You should have received a copy of the GNU General Public License    #
#  along with gazix. If not, see <https://www.gnu.org/licenses/>.       #
#                                                                       #
#########################################################################

from ..api.gitlab_api_access import *
from ..api.gitlab_api_queries import *
from ..arguments.arguments import *
from ..utils.option import *
from ..utils.log import *
from ..api.gitlab_api_pipeline import *
from ..api.gitlab_api_MR import *

labels_program = "kill"


class Kill:

    def __init__(self, arguments):
        self._help = False
        _gitlab_api_url = None
        _token = None
        _project = None
        self._pipeline = None
        for i in range(len(arguments)):
            if option(arguments[i], gitlab_api_url):
                _gitlab_api_url = arguments[i + 1]
                i += 1
            if option(arguments[i], token):
                _token = arguments[i + 1]
                i += 1
            elif option(arguments[i], project):
                _project = arguments[i + 1]
                i += 1
            elif option(arguments[i], pipeline):
                self._pipeline = arguments[i + 1]
                i += 1
            elif option(arguments[i], help_short, help_long):
                self._help = True
        self._access = GitLabAPIAccess(_gitlab_api_url, _token, _project)
        self._queries = GitLabAPIQueries(self._access)
        if self._help:
            self.help(gazix, labels_program)
            exit(0)
        if not self._access.is_valid():
            self.help(gazix, labels_program)
            exit(1)
        exit(self.kill())

    def kill(self):
        print("Killing pipeline " + self._pipeline)
        pipeline = GitlLabAPIPipeline(self._pipeline)
        self._queries.post(obj=pipeline, query="cancel")
        return 0

    def help(self, gazix="", program=""):
        print(gazix + " " + program + " [options]")
        print("\toptions:")
        print("\t-h/--help                Print the help")
        print("\t--gitlab [value]         Gitlab API url of the repository")
        print("\t--token [value]          Token of the repository")
        print("\t--project [value]        ID of the repository")
        print("\t--pipeline [value]       Current pipeline ID of the repository")
