def twoTeams(students):
    return (sum(students[i] for i in range(len(students)) if i%2==0)-sum(students[i] for i in range(len(students)) if i%2!=0))
