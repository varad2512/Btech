#Tutorial 1 Ring Algorithm DC
from llist import sllist
from random import randint
jobs = []
print "Enter the number of processes"
n = raw_input()
for x in range(int(n)):
	jobs.append(tuple(int(x) for x in raw_input().split(',')))
initial_coordinator = max(jobs,key=lambda x:x[1])
print "initial_coordinator : Process ",initial_coordinator
index = 0
for x in jobs:
	if x == initial_coordinator:
		break
	index = index + 1
jobs[index] = (jobs[index][0],jobs[index][1],0,jobs[index][3])
dead = min(jobs,key = lambda x:x[2])
priorities = []
ll = sllist()
for x in jobs:
	ll.append(x)
initial = randint(0,len(ll)-2)
print "Random initializer :", initial
for x in range(len(ll) - 1):
	print "loop initial",initial
	priorities.append(ll[initial][1])
	print "Election message from process : ",ll[initial][0],"to",
	if ll[ll[initial][3]-1][2] != 0:
		initial = ll[initial][3] - 1
		print "if",initial
	else:
		initial = ll[ll[initial][3] - 1][3] - 1
		print "else",initial
	print ll[initial][0]
print priorities
max_priority = max(priorities)
find = 0
for x in ll:
	if x[1] == max_priority:
		break
	find = find + 1 
print "New coordinator is :",ll[find]
initial1 = find 
for x in range(len(ll)-1):
	print "Communication message from process : ",ll[initial1][0],"to",
	initial1 = ll[initial1][3] - 1
	print ll[initial1][0]