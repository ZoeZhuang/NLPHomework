import numpy as np
# -*- codeing:utf-8 -*-


#   隐状态
hidden_state = ['start','v', 'n','adv','end']

#   观测序列
obsevition = ['beging','learning', 'changes', 'throughly','stop']


#   根据观测序列、发射概率、状态转移矩阵、发射概率
#   返回最佳路径
def compute(obs, states, start_p, trans_p, emit_p):
    #   max_p（3*2）每一列存储第一列不同隐状态的最大概率
    max_p = np.zeros((len(obs), len(states)))

    #   path（2*3）每一行存储上max_p对应列的路径
    path = np.zeros((len(states), len(obs)))

    #   初始化
    for i in range(len(states)):
        max_p[0][i] = start_p[i] * emit_p[i][obs[0]]
        path[i][0] = i

    for t in range(1, len(obs)):
        print(t)
        print('\n')
        newpath = np.zeros((len(states), len(obs)))
        for y in range(len(states)):
            prob = -1
            for y0 in range(len(states)):
                nprob = max_p[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]]
#                 if nprob != 0.0:
#                     print(nprob)
#                     print('\n')
                if nprob > prob:
                    prob = nprob
                    state = y0
                    #   记录路径
                    max_p[t][y] = prob
                    for m in range(t):
                        newpath[y][m] = path[state][m]
                    newpath[y][t] = y

        path = newpath

    for kk in range(len(obs)):
        for tt in range(len(states)):
            print(max_p[kk][tt])
            print('       ')
        print('\n')
    max_prob = -1
    path_state = 0
    #   返回最大概率的路径
    for y in range(len(states)):
        if max_p[len(obs)-1][y] > max_prob:
            max_prob = max_p[len(obs)-1][y]
            path_state = y

    return path[path_state]

state_s = [0, 1, 2, 3, 4]
obser = [0, 1, 2, 3,4]

#   初始状态，测试集中，0.6概率观测序列以sunny开始
start_probability = [1, 0 ,0 ,0 ,0]

#   转移概率，0.7：sunny下一天sunny的概率
transititon_probability = np.array([[0,0.3,0.2,0,0],
                                    [0,0.1,0.4,0.4,0],
                                    [0,0.3,0.1,0.1,0],
                                    [0,0,0,0,0.1],
                                    [0,0,0,0,0]])

#   发射概率，0.4：sunny在0.4概率下为shop
emission_probability = np.array([[1,0,0,0,0],
                                 [0,0.003,0.004,0,0],
                                 [0,0.001,0.003,0,0],
                                 [0,0,0,0.002,0],
                                 [1,1,1,1,1]])

result = compute(obser, state_s, start_probability, transititon_probability, emission_probability)

for k in range(len(result)):
    print(hidden_state[int(result[k])])