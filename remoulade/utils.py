# This file is a part of Remoulade.
#
# Copyright (C) 2017,2018 WIREMIND SAS <dev@wiremind.fr>
#
# Remoulade is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# Remoulade is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

global_scheduler = None


def get_scheduler():
    global global_scheduler
    if global_scheduler is None:
        raise ValueError("Scheduler not found, are you sure you called set_scheduler(scheduler) ?")
    return global_scheduler


def set_scheduler(scheduler):
    global global_scheduler
    global_scheduler = scheduler