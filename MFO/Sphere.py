import numpy as np


class Sphere:
    """
    问题
    """

    def __init__(self, x_dim=1, x_min=-100, x_max=100):
        self.x_dim = x_dim
        self.x_min = x_min
        self.x_max = x_max

    def generate_feasible_solutions(self, n=1):
        """
        生成可行解
        :return: 可行解
        """

        x = self.x_min + np.random.rand(n, self.x_dim) * (self.x_max - self.x_min)

        return x

    @staticmethod
    def calculate_fitness_value(x):
        """
        计算目标函数值
        :param x: 自变量
        :return: 函数值
        """

        y = (x ** 2).sum(1)

        return y

    @staticmethod
    def compare_fitness_value(y1, y2):
        """
        比较目标函数值
        :param y1: 目标值1
        :param y2: 目标值2
        :return: 0 相等 1 y1优于y2 -1 y2优于y1
        """

        if y1[0] < y2[0]:
            return 1
        elif y1[0] == y2[0]:
            return 0
        else:
            return -1


def test():
    """
    test function
    :return:
    """

    problem = Sphere(2)
    x = problem.generate_feasible_solutions(10)
    print('===x===')
    print(x)

    y = problem.calculate_fitness_value(x)
    print('===y===')
    print(y)


if __name__ == '__main__':
    test()
