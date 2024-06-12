class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while sandwiches and students:
            if sandwiches == [] and students == []:
                return 0
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)

            else:
                student = students.pop(0)
                students.append(student)

            if sandwiches:
                if sandwiches[0] not in students:
                    break


            print(sandwiches, students)
        
        return len(students)
