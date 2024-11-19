class Task:
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish

tasks = [
    Task("book", 9, 12),
    Task("laptop", 1, 5),
    Task("headphones", 3, 8),
    Task("tablet", 2, 4),
    Task("charger", 6, 7),
    Task("notebook", 13, 16),
    Task("pen", 10, 14),
    Task("bag", 15, 18),
    Task("bottle", 11, 17)
]

tasks.sort(key=lambda t: t.finish, reverse=True)

print("Topological Sort:")
for task in tasks:
    print(task.name)
