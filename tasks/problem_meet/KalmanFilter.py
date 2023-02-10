# -*- coding: utf-8 -*-
# @Time : 2022/9/6 14:13
# @Author : Zhangzixu
# @Software: PyCharm
# @Description: 卡曼尔滤波蒜贩
import numpy


class KalmanFilter(object):
    """
    卡曼尔滤波算法
    """

    def __init__(self, fundamental_vector_matrix=None, start_point_value=None,
                 deformation_matrix=None, gradient_matrix=None, R=None, P=None):
        if fundamental_vector_matrix is None or deformation_matrix is None:
            raise ValueError("please input value")

        self.matrix_row = fundamental_vector_matrix.shape[1]
        self.deformation_matrix = deformation_matrix.shape[1]

        self.fundamental_vector_matrix = fundamental_vector_matrix
        self.deformation_matrix = deformation_matrix
        self.start_point_value = 0 if start_point_value is None else start_point_value
        self.gradient_matrix = numpy.eye(self.matrix_row) if gradient_matrix is None else gradient_matrix
        self.R = numpy.eye(self.matrix_row) if R is None else R
        self.P = numpy.eye(self.matrix_row) if P is None else P
        self.x = numpy.zeros((self.matrix_row, 1)) if start_point_value is None else start_point_value

    def predict(self, u=0):
        self.x = numpy.dot(self.fundamental_vector_matrix, self.x) + numpy.dot(self.start_point_value, u)
        self.P = numpy.dot(numpy.dot(self.fundamental_vector_matrix, self.P),
                           self.fundamental_vector_matrix.T) + self.gradient_matrix
        return self.x

    def update(self, z):
        y = z - numpy.dot(self.deformation_matrix, self.x)
        S = self.R + numpy.dot(self.deformation_matrix, numpy.dot(self.P, self.deformation_matrix.T))
        K = numpy.dot(numpy.dot(self.P, self.deformation_matrix.T), numpy.linalg.inv(S))
        self.x = self.x + numpy.dot(K, y)
        I = numpy.eye(self.matrix_row)
        self.P = numpy.dot(numpy.dot(I - numpy.dot(K, self.deformation_matrix), self.P),
                           (I - numpy.dot(K, self.deformation_matrix)).T) + numpy.dot(numpy.dot(K, self.R), K.T)


if __name__ == '__main__':
    dt = 1.0 / 8000
    fundamental_vector_matrix = numpy.array([[0.8, dt, 0], [0, 1, dt], [0, 1, 1]])
    deformation_matrix = numpy.array([1, 0, 0]).reshape(1, 3)
    gradient_matrix = numpy.array([[0.05, 0.05, 0.0], [0.05, 0.05, 0.0], [0.0, 0.0, 0.0]])
    R = numpy.array([1]).reshape(1, 1)
    kf = KalmanFilter(fundamental_vector_matrix=fundamental_vector_matrix,
                      deformation_matrix=deformation_matrix,
                      start_point_value=1,
                      gradient_matrix=gradient_matrix, R=R)

    # start
    predictions = []
    a = {"20220606":353,"20220607":351,"20220608":349,"20220609":347,"20220610":345,"20220611":343,"20220612":341,"20220613":339,"20220614":337,"20220615":335,"20220616":333,"20220617":331,"20220618":327,"20220619":323,"20220620":319,"20220621":315,"20220622":312,"20220623":312,"20220624":312,"20220625":312,"20220808":4,"20220809":4,"20220810":4,"20220811":4,"20220812":4,"20220813":4,"20220814":4,"20220815":10,"20220816":6,"20220817":6,"20220818":6,"20220819":6,"20220820":6,"20220821":6,"20220822":6,"20220823":6,"20220824":6,"20220825":6,"20220826":6,"20220827":4,"20220828":4,"20220829":4}
    m1 = [3, 4, 5, 6, 71, 2, 344, 6, 6, 137, 27, 22]
    m2 = [2, 9, 6, 6, 10, 27, 21]
    m3 = a.values()
    for item in m3:
        predictions.append(numpy.dot(numpy.array([1, 0, 0]).reshape(1, 3),
                                     kf.predict())[0])
        kf.update(item)


    result = [x[0] for x in numpy.array(predictions)]
    print(result)
    print(sum(result))

    seven_order_history = []
    seven_order = 0
    for index in range(len(result)):
        if index <= 5:
            seven_order += result[index]
        else:
            seven_order += result[index]
            seven_order_history.append(seven_order)
            seven_order -= result[index - 6]

    print(seven_order_history)
    print(seven_order)

    import ujson
    while len(ujson.dumps(a).replace(" ", "")) > 256:
        a = dict(sorted(a.items(), key=lambda d: d[0])[1:])

    print(a)
