"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

"""
from collections import defaultdict


def get_course_order(prerequisites_map: dict):
    course_map = defaultdict(set)
    total_courses_set = set()
    initial_courses_set = set()
    for course, prerequisites in prerequisites_map.items():
        total_courses_set.add(course)
        total_courses_set.update(prerequisites)
        if not prerequisites:
            initial_courses_set.add(course)
        for prerequisite in prerequisites:
            course_map[prerequisite].add(course)
    prerequisites_map['SOURCE'] = []
    final_courses_set = total_courses_set.difference(course_map.keys())
    prerequisites_map['TARGET'] = final_courses_set
    course_map['SOURCE'] = initial_courses_set
    for course in final_courses_set:
        course_map[course].add("TARGET")

    # Run BFS
    course_order = []
    queue = ['SOURCE']
    queue_set = {'SOURCE'}
    visited = set()
    while queue:
        node = queue.pop(0)
        queue_set.remove(node)
        for prerequisite in prerequisites_map[node]:
            if prerequisite not in visited:
                queue.append(node)
                queue_set.add(node)
                break
        else:
            visited.add(node)
            course_order.append(node)
            for adjacent_node in course_map[node]:
                if adjacent_node not in visited:
                    if adjacent_node not in queue_set:
                        queue.append(adjacent_node)
                        queue_set.add(adjacent_node)
                    else:
                        continue
                else:
                    return None

    return course_order[1:-1] if len(course_order)>2 else None


print(get_course_order({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}))
print(get_course_order({'CSC200': ['CSC100'], 'CSC100': ['CSC200']}))