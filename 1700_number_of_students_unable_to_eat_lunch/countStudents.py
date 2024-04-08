from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        want = True

        while want:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)

            else:
                student = students.pop(0)
                students.append(student)

            if not len(sandwiches):
                want = False

            if len(sandwiches) and sandwiches[0] not in students:
                want = False

        return len(students)