from onsite.observation import Observation
import pandas as pd
import numpy as np
from functools import reduce


class DataRecord():
    def __init__(self):
        self.data = {}
        self.vehicle_column = ['x', 'y', 'v', 'yaw', 'width', 'length']

    def add_data(self, observation: Observation):
        """将输入的观察值进行存储

        """
        # 首先将已经建立了对应DataFrame的车辆名提取出来
        stored_vehicles = self.data.keys()

        # 提取observation对应的时刻
        t = observation.test_setting['t']

        # 遍历observation中的所有车辆
        for vehicle_name, values in observation.vehicle_info.items():
            # 如果vehi_name对应的车还没有建立DataFrame,则先建立
            if vehicle_name not in stored_vehicles:
                self._add_vehicle_frame(vehicle_name)

            # 为t时刻的数据建立当前时刻的DataFrame
            sub_frame = pd.DataFrame(
                values,
                columns=self.vehicle_column,
                index=[t]
            )
            # 修改列名，便于合并
            sub_frame.columns = list(self.data[vehicle_name].columns)
            # 将当前时刻的DataFrame加入车辆的DataFrame中
            self.data[vehicle_name] = pd.concat([self.data[vehicle_name], sub_frame])

    def merge_frame(self) -> pd.DataFrame:
        """将存储的所有交通参与者的DataFrame，按照时间进行合并，返回完整的DataFrame

        """
        # 取出每辆车的DataFrame，组成列表
        vehicle_dataframe_group = [self.data[vehi_name]
                                   for vehi_name in list(self.data.keys())]
        # 返回合并后的DataFrame
        return reduce(lambda x, y: pd.merge(x, y, how="outer", left_index=True, right_index=True), vehicle_dataframe_group)

    def _add_vehicle_frame(self, vehicle_name: str):
        """为某一交通参与者创造对应的小DataFrame

        """
        self.data[vehicle_name] = pd.DataFrame(
            None,
            columns=[i + "_" + str(vehicle_name) for i in self.vehicle_column]
        )


class Recorder():
    """记录场景运行信息

    """

    def __init__(self):
        self.output_dir = ""
        self.file_name = ""
        self.data_record = DataRecord()

    def init(self, observation: Observation, output_dir: str) -> None:
        if output_dir[-1] != "/":
            output_dir += "/"
        # 创建新的数据容器，目的是删除之前的数据
        self.data_record = DataRecord()
        self.output_dir = output_dir
        self.record(observation)

    def record(self, observation: Observation) -> None:
        """记录当前时刻的运行信息，如果发现end status表示为测试结束，则写入文件。

        """
        # 记录当前时刻的数据
        self.data_record.add_data(observation)
        # 合并。
        data_output = self.data_record.merge_frame()
        # 增加结束状态一列
        data_output.loc[:, 'end'] = -1
        # 将最后一个值调整为观察值中的end，若-1则表示规控器问题导致测试不能顺利结束，若1则表示到达最大时间结束，若2则说明发生碰撞
        data_output.iloc[-1, -1] = observation.test_setting['end']
        # 写入文件，每一步都会写入，自动覆盖上一步的文件
        data_output.to_csv(
            self.output_dir + observation.test_setting['scenario_name'] + ".csv")
        # 如果测试不是中途结束，即不是规控器自身的问题，那么会打印输出test_setting。
        if observation.test_setting['end'] != -1:
            print(observation.test_setting)


if __name__ == "__main__":
    data = DataRecord()
    observe = Observation()
    data.add_data(observe)
    print(data.data)
