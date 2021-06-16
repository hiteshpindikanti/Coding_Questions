from unittest import TestCase, main as run_unit_tests

memo = {}


def is_match(string: str, pattern: str) -> bool:
    if (string, pattern) not in memo.keys():
        if len(string) == len(pattern) == 0:
            memo[(string, pattern)] = True
        elif pattern and string and (string[0] == pattern[0] or pattern[0] == '.'):
            if (len(pattern) > 1 and pattern[1] != '*') or len(pattern) == 1:
                memo[(string, pattern)] = is_match(string[1:], pattern[1:])
            else:
                memo[(string, pattern)] = is_match(string[1:], pattern) or \
                                          is_match(string[1:], pattern[2:]) or \
                                          is_match(string[:], pattern[2:])
        elif len(pattern) > 1 and pattern[1] == '*':
            memo[(string, pattern)] = is_match(string[:], pattern[2:])
        else:
            memo[(string, pattern)] = False
    print(f'memo[({string}, {pattern})] = {memo[(string, pattern)]}')
    return memo[(string, pattern)]


def is_match_iterative(string: str, pattern: str) -> bool:
    pattern = convert_pattern_to_list(pattern)
    is_match_cache = [[None] * len(pattern) for _ in range(len(string))]
    stack = [[(0, 0)]]
    while stack:
        call_list = stack.pop()
        for i, j in call_list:
            if string[i] == pattern[j][0] or pattern[j][0] == '.':
                if len(pattern[j]) == 1:
                    if is_match_cache[i+1][j+1] is not None:
                        is_match_cache[i][j] = is_match_cache[i+1][j+1]
                    else:
                        stack.append(call_list)
                        stack.append([(i+1, j+1)])
                        continue
                else:
                    pass

    return False


def convert_pattern_to_list(pattern: str) -> list[str]:
    pattern_list = []
    i = 0
    while i < len(pattern)-1:
        if pattern[i+1] == '*':
            pattern_list.append(pattern[i:i+2])
        else:
            pattern_list.append(pattern[i])
    return pattern_list


class RegexTestCases(TestCase):
    def test_negative_1(self):
        self.assertFalse(is_match('aa', 'a'))

    def test_positive_1(self):
        self.assertTrue(is_match('aa', 'a*'))

    def test_positive_2(self):
        self.assertTrue(is_match('aa', '.*'))

    def test_positive_3(self):
        self.assertTrue(is_match('aab', 'c*a*b'))

    def test_positive_4(self):
        self.assertTrue(is_match('ab', 'c*a*b*c*d*'))

    def test_positive_5(self):
        self.assertTrue(is_match("bbbba", ".*a*a"))

    def test_negative(self):
        self.assertFalse(is_match("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))


if __name__ == "__main__":
    print(is_match('aab', 'c*a*b'))
    # run_unit_tests()
    pass
