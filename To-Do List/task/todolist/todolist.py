# Write your code here
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()

today = datetime.today()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=today.date())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def print_todays_tasks():
    tasks = session.query(Task)\
        .filter(Task.deadline == today.date())\
        .all()
    print(f"Today {today.day} {today.strftime('%b')}:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
    if len(tasks) == 0:
        print("Nothing to do!")


def print_weeks_tasks():
    for d in range(7):
        task_date = today + timedelta(days=d)
        tasks = session.query(Task)\
            .filter(Task.deadline == task_date.date())\
            .all()
        print(f"{task_date.strftime('%A')} {task_date.day}",
              f"{task_date.strftime('%b')}:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        if len(tasks) == 0:
            print("Nothing to do!")
        print()


def print_all_tasks():
    tasks = session.query(Task)\
        .order_by(Task.deadline)\
        .all()
    print("All tasks:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}.",
              f"{tasks[i].deadline.day} {tasks[i].deadline.strftime('%b')}")
    if len(tasks) == 0:
        print("Nothing to do!")


def print_missed_tasks():
    tasks = session.query(Task)\
        .filter(Task.deadline < today.date())\
        .order_by(Task.deadline)\
        .all()
    print("Missed tasks:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}.",
              f"{tasks[i].deadline.day} {tasks[i].deadline.strftime('%b')}")
    if len(tasks) == 0:
        print("Nothing is missed!")


def add_task():
    print("Enter task")
    new_task_str = input()
    print("Enter deadline")
    new_task_deadline = datetime.strptime(input(), "%Y-%m-%d")
    new_row = Task(task=new_task_str,
                   deadline=new_task_deadline)
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def delete_task():
    tasks = session.query(Task)\
        .order_by(Task.deadline)\
        .all()
    if len(tasks) == 0:
        print("Nothing to delete")
    else:
        print("Choose the number of the task you want to delete:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}.",
                  f"{tasks[i].deadline.day}",
                  f"{tasks[i].deadline.strftime('%b')}")
        delete_task_idx = int(input()) - 1
        session.delete(tasks[delete_task_idx])
        session.commit()
        print("The task has been deleted!")


choice = -1
while choice != 0:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    choice = int(input())
    if choice == 1:
        print_todays_tasks()
    elif choice == 2:
        print_weeks_tasks()
    elif choice == 3:
        print_all_tasks()
    elif choice == 4:
        print_missed_tasks()
    elif choice == 5:
        add_task()
    elif choice == 6:
        delete_task()
    elif choice == 0:
        print("Bye!")
    else:
        print("Wrong choice!")
    print()
