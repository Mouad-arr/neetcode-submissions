class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(students)
        i,j=0,0
        num=0
        student=set()
        first=-1
        while j<n:
            if students[i]==sandwiches[j] and i not in student:
                j+=1
                student.add(i)
                first=-1
            if first==i:
                break
            if first==-1:
                first=i
            i+=1
            i = i%n
        return n - len(student)