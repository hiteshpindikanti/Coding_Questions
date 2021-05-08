from collections import defaultdict

gamma = 0.9
reward = defaultdict(float)
reward[(4, 5)] = 5
reward[(1, 2)] = -5

failure_targets = {(0, 1): (0, 3),
                   (0, 3): (0, 1),
                   (1, 0): (1, 4),
                   (1, 4): (0, 2),
                   (1, 2): (1, 4),
                   (3, 0): (3, 4),
                   (3, 4): (3, 0),
                   (4, 5): (4, 1),
                   (4, 1): (3, 5),
                   (4, 3): (4, 1)}


def value(source_state, target, prev_v) -> float:
    fail_target = failure_targets[(source_state, target)]
    val = 0.8 * (reward[(source_state, target)] + gamma * prev_v[target]) + \
          0.1 * (reward[(source_state, fail_target[0])] + gamma * prev_v[fail_target[0]]) + \
          0.1 * (reward[(source_state, fail_target[1])] + gamma * prev_v[fail_target[1]])
    # print("{}->{} : {} | ".format(source_state, target, val), end="")
    return val


def value_iteration():
    # initial v_0
    v_i = [0.0] * 6
    i = 0
    prev_sum = float('inf')
    while abs(sum(v_i) - prev_sum) > 0.0000001:
        i += 1
        new_v = [0.0] * 6
        new_v[0] = max(value(0, 1, v_i), value(0, 3, v_i))
        #print()
        new_v[1] = max(value(1, 0, v_i), value(1, 2, v_i), value(1, 4, v_i))
        #print()
        new_v[3] = max(value(3, 0, v_i), value(3, 4, v_i))
        #print()
        new_v[4] = max(value(4, 3, v_i), value(4, 5, v_i), value(4, 1, v_i))
        #print()
        print("V_{} = {}".format(i, new_v))
        prev_sum = sum(v_i)
        v_i = new_v

value_iteration()