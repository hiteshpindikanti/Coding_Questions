import numpy as np


class Problem:
    def __init__(self, initial_prob, transition_prob, emission_prob, observe_seq):
        self.initial_prob = initial_prob  # pi
        self.transition_prob = transition_prob  # a
        self.emission_prob = emission_prob  # b
        self.observe_seq = observe_seq  # o
        self.num_states = len(self.initial_prob)
        self.num_observations = len(self.observe_seq)

    def get_alpha(self, state, time, verbose=False):
        alpha = [[self.emission_prob[s][self.observe_seq[0]] * self.initial_prob[s] for s in range(self.num_states)]]
        if time == 1:
            return alpha[-1][state]
        for t in range(1, time - 1):
            alpha.append([self.emission_prob[s2][self.observe_seq[t]] * sum(
                [self.transition_prob[s1][s2] * alpha[-1][s1] for s1 in range(self.num_states)]) for s2 in
                          range(self.num_states)])
        final_alpha = self.emission_prob[state][self.observe_seq[time - 1]] * sum(
            [self.transition_prob[s1][state] * alpha[-1][s1] for s1 in range(self.num_states)])
        if verbose:
            for t, a1 in enumerate(alpha):
                for s, a2 in enumerate(a1):
                    print(f"alpha_s{s + 1}(t={t + 1})={a2}")
            print(f"alpha_s{state + 1}(t={time})={final_alpha}\n")
        return final_alpha

    def get_delta(self, state, time, verbose=False):
        delta = [[self.get_alpha(s, 1) for s in range(self.num_states)]]
        if time == 1:
            return delta[-1][state]
        for t in range(1, time - 1):
            delta.append([self.emission_prob[s2][t] * max(
                [delta[-1][s1] * self.transition_prob[s1][s2] for s1 in range(self.num_states)]) for s2 in
                          range(self.num_states)])
        arg_max, max_val = max(
            [(s1, delta[-1][s1] * self.transition_prob[s1][state]) for s1 in range(self.num_states)],
            key=lambda x: x[1])
        final_delta = self.emission_prob[state][self.observe_seq[time - 1]] * max_val
        if verbose:
            for t, a1 in enumerate(delta):
                for s, a2 in enumerate(a1):
                    print(f"delta_s{s + 1}(t={t + 1})={a2}")
            print(f"delta_s{state + 1}(t={time})={final_delta}, arg_max_state=s{arg_max + 1}\n")
        return arg_max, final_delta


if __name__ == "__main__":
    pi = [0.6, 0.4]
    A = [[0.7, 0.3],
         [0.2, 0.8]]
    B = [[0.4, 0.1, 0.4, 0.1],
         [0.2, 0.3, 0.2, 0.3]]
    O = [0, 2, 1, 3]  # [A, G, C, T]

    problem = Problem(pi, A, B, O)
    # print(f"Problem 3.1 Answer = {problem.get_alpha(0, 4, verbose=True) + problem.get_alpha(1, 4, verbose=True)}")

    problem.get_delta(0, 2, verbose=True)
    problem.get_delta(1, 2, verbose=True)
    problem.get_delta(0, 3, verbose=True)
    problem.get_delta(1, 3, verbose=True)
    problem.get_delta(0, 4, verbose=True)
    problem.get_delta(1, 4, verbose=True)

    # print(f"Problem 3.2 Answer = {problem.get_delta(0, 1)}")
