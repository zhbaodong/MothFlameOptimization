from TestFunction import TestFunction


class MFO:

    """飞蛾扑火优化算法"""

    def __init__(self, size, max_iter, problem):
        """
        :param size: 飞蛾数量
        :param max_iter: 最大迭代次数
        :param problem: 问题
        """
        self.size = size
        self.max_iter = max_iter
        self.problem = problem

        # 初始化飞蛾种群
        self.M = problem.generate_feasible_solutions(size)

        # 计算种群适应度值
        self.OM = problem.calculate_fitness_value(self.M)

        # 初始化火焰适应度值
        self.OF = self.OM.copy()

        # 火焰排序
        index = self.OF.argsort()
        self.OF.sort()

        # 初始化火焰
        self.F = self.M.copy()
        for i in range(self.OF.shape[0]):
            self.F[i] = self.M[index[i]]

    def solve(self):
        """
        求解
        """

        print('MFO is optimizing your problem')

        for i in range(100):
            print('===%d===' % i)
            for j in range(self.size):
                self.population[j].update(self.gBest)
                if self.problem.compare_fitness_value(self.population[j].fit, self.gFit) > 0:
                    self.gBest = self.population[j].x.copy()
                    self.gFit = self.population[j].fit.copy()
                print('x: %f v: %f fit: %f' % (self.population[j].x, self.population[j].v, self.population[j].fit))
            print("gBest: %f gFit: %f" % (self.gBest, self.gFit))


def test():
    """
    test function
    :return:
    """

    problem = TestFunction('F1')
    mfo = MFO(30, 1000, problem)

    print('===M===')
    print(mfo.M)

    print('===OM===')
    print(mfo.OM)

    print('===F===')
    print(mfo.F)

    print('===OF===')
    print(mfo.OF)


if __name__ == '__main__':
    test()
