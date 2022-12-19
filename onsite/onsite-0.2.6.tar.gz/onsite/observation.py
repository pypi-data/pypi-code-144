import numpy as np
import pandas as pd


class Observation():
    """
    vehicle_info={
        "ego":{
            "x":,
            "y":,
            "v":,
            "yaw":,
            "width":,
            "length":,
        },
        "0":{...},
        ...
    }
    test_setting = {
            "t":,
            "dt":,
            "max_t",
            "goal":,
            "end":
        }
    """

    def __init__(self):
        self.vehicle_info = {
            "ego": {
                "x": -1,
                "y": -1,
                "v": -1,
                "yaw": -1,
                "width": -1,
                "length": -1
            },
        }
        self.road_info = {}
        self.test_setting = {
            "scenario_name": "name",
            "scenario_type": "replay",
            "t": 0.00,
            "dt": -1,
            "max_t": -1,
            "goal": {
                "x": [-1, -1],
                "y": [-1, -1]
            },
            "end": -1
        }


if __name__ == "__main__":
    pass
