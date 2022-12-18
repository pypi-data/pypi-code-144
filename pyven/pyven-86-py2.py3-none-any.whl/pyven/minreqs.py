# Copyright 2013, 2014, 2015, 2016, 2017, 2020, 2022 Andrzej Cichocki

# This file is part of pyven.
#
# pyven is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyven is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyven.  If not, see <http://www.gnu.org/licenses/>.

'Print project.arid snippet pinning requires to their minimum allowed versions.'
from .projectinfo import ProjectInfo
from venvpool import initlogging

def main():
    initlogging()
    print("requires = $list(%s)" % ' '.join(r.minstr() for r in ProjectInfo.seek('.').parsedrequires()))

if '__main__' == __name__:
    main()
