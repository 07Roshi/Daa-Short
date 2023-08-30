from collections import defaultdict
class Graph:
    def __init__(self, subjects):
        self.subjects, self.graph = subjects, defaultdict(list)
    def addedge(self, s1, s2):
        self.graph[s1].append(s2)
        self.graph[s2].append(s1)
    def coloring(self):
        cm, ac = {}, set(range(1, len(self.subjects) + 1))
        for i in self.subjects:
            uc = {cm[n] for n in self.graph[i] if n in cm}
            acolor = ac - uc
            cm[i]=min(acolor) if acolor else len(ac)+1
            ac.add(cm[i])
        return cm
    def timeslots(self):
        return max(self.coloring().values())
n = int(input("Enter the number of subjects: "))
sub, stu= [], {}
for i in range(n):
    subject = input(f"Enter subject {i + 1}: ")
    sub.append(subject)
    n_st = int(input(f"Enter the number of students for {subject}: "))
    st_list = [input(f"Enter student {j + 1} for {subject}: ") for j in range(n_st)]
    stu[subject] = st_list
g=Graph(sub)
for _ in range(int(input("Enter the number of edges: "))):
    e = input("Enter edge (subject1 subject2): ").split()
    g.addedge(e[0], e[1])
print(f"\nMinimum time slots needed: {g.timeslots()}")


"""Enter the number of subjects: 4
Enter subject 1: maths
Enter the number of students for maths: 3
Enter student 1 for maths: alice
Enter student 2 for maths: bob
Enter student 3 for maths: charlie
Enter subject 2: physics
Enter the number of students for physics: 3
Enter student 1 for physics: alice
Enter student 2 for physics: charlie
Enter student 3 for physics: david
Enter subject 3: chemistry
Enter the number of students for chemistry: 3
Enter student 1 for chemistry: bob
Enter student 2 for chemistry: charlie
Enter student 3 for chemistry: eve
Enter subject 4: biology
Enter the number of students for biology: 3
Enter student 1 for biology: alice
Enter student 2 for biology: david
Enter student 3 for biology: eve
Enter the number of edges: 4
Enter edge (subject1 subject2): maths physics
Enter edge (subject1 subject2): maths chemistry
Enter edge (subject1 subject2): physics chemistry
Enter edge (subject1 subject2): physics biology

Minimum time slots needed: 3
"""