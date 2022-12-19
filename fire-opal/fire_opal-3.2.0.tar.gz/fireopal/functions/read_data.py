# Copyright 2022 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.


from .base import fire_opal_workflow


@fire_opal_workflow("read_database_workflow")
def read_data(
    ibm_device_name: str,
    entry: str,
):
    """Reads an entry from the Fire Opal database."""
    return {
        "ibm_device_name": ibm_device_name,
        "entry": entry,
    }
