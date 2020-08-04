import numpy as np
# y = wx + b : 线性回归实例。
#第一步：计算损失函数
def computer_error_for_line_given_points(b,w,points):
    totalError = 0
    for i in range(len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError += ((w * x + b)-y) ** 2
    return totalError / float(len(points))

#Computer Gradient and update
#第二步：计算梯度和更新
def step_gradient(b_current,w_current,points,learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        #grad_b = 2(wx+b-y)
        #grad_w = 2(wx+b-y)*x
        b_gradient += (2/N) * ((w_current * x + b_current) - y)
        w_gradient += (2/N) * x * ((w_current * x + b_current) - y)
    #更新
    new_b = b_current - (learningRate * b_gradient)
    new_w = w_current - (learningRate * w_gradient)
    return [new_b,new_w]

#第三步将更新后的值赋给w和b；循环
#num_iterations是循环次数
def gradient_descent_runner(points,starting_b,starting_w,learning_rate,num_iterations):
    b = starting_b
    w = starting_w
    for _ in range(num_iterations):
        b,w = step_gradient(b,w,np.array(points),learning_rate)
    return [b,w]

def run():
    points = np.genfromtxt("data/linear_data.csv",delimiter=",")
    learning_rate = 0.0001
    initial_b = 0
    initial_w = 0
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, w = {1}, error = {2}"
          .format(initial_b,initial_w,
                  computer_error_for_line_given_points(initial_b,initial_w,points)
                  )
          )
    print("Running")
    [b,w] = gradient_descent_runner(points,initial_b,initial_w,learning_rate,num_iterations)
    print("After {0} iterations b = {1}, w = {2}, error = {3}".
          format(num_iterations, b, w,
                 computer_error_for_line_given_points(b, w, points))
          )

if __name__ == '__main__':
    run()