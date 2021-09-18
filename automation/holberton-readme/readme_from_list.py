#!/usr/bin/env python3
"""Module containing functions for creating a README.md file for Holberton
School projects."""



def get_project_title():
    """Takes the current working directory of a holberton project and returns the
    title of the project."""
    import os
    directory = os.getcwd()
    temp = directory.copy()
    project_reop = temp.split("/")[-1]
    container_repo = temp[-3] + "/" + temp[-2]
    title = temp[-1].split("-")[-1].title().replace("-", " ")
    return title

class Task():
    """Individual task as part of a project.
    """
    # Class attributes
    total_tasks = 0
    
    # Magic methods
    def __init__(self, name="", description="", file="") -> None:
        self.__number = Task.total_tasks
        Task.total_tasks += 1
        self.__name = name
        self.__description = description
        self.__file = file
    
    # Getters and setters
    @property
    def number(self) -> int:
        return self.__number
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def file(self) -> list:
        return self.__file

def get_tasks() -> list:
    """Prompts user for information, then uses it to create objects for each
    task in the project."""
    tasks = []
    go_on = True
    confirm = ""

    while go_on:
        name = input("Task Name: ")
        # description = input("Task description: ")
        description = "Description goes here once I figure out clipboard input."
        file = input("File name: ")

        print("Task name: {}".format(name))
        print("Description: {}".format(description))
        print("File: {}".format(file))
        while confirm != "y" and confirm != "n":
            confirm = input("Is this correct? y/n: ").lower()
            print("Your answer was: {}".format(confirm))
        if confirm == "y":
            tasks.append(Task(name=name, description=description, file=file))
            print("Task added")
        else:
            print("Task not added")

        while go_on != "y" and go_on != "n":
            go_on = input("Add more tasks? y/n: ").lower()
        if go_on == "n":
            break
        go_on = True
        confirm = ""

    return tasks

def get_leanring_objectives() -> str:
    """Asks user for learning objectives and formats them."""
    done = False
    while not done:
        objectives = input("Learning Objectives: ").split("\n")
        formated = ""
        for each in objectives:
            formated += "* " + each + "\n"
        print("Objectives: {}".format(formated))
        while done != "y" and done != "n":
            done = input("Is this correct? y/n: ").lower()
        if done == "y":
            print("Learning objectives confirmed")
            return formated
        else:
            done = False

def create_readme(project, learning="", tasks=[]) -> None:
    """Takes the project name, learning objectives, and tasks, then
    writes them into the README.md file accoriding to template.

    Args:
        project (str): Name of the project for the README.md file.
        tasks (list, optional): List of tasks for the project. Defaults to [].
        learning (str, optional): Learning objectives for the project. Defaults to "".
    """
    title = "# " + project
    table =  (
        "\n\n1. [Learning Objectives](#learning-objectives)\n2. " +
        "[References](#references)\n3. [Tasks](#tasks)\n"
    )
    count = 0
    for task in tasks:
        count += 1
        table += "\t{}. [{}](#{}-{})\n".format(
                count, task.name, task.number,
                task.name.lower().replace(" ", "-")
            )
    table += "\n"
    learning_objectives =  (
        "## Learning Objectives\nAt the end of this project, you are " + 
        "expected to be able to explain to anyone, without the help of " +
        "Google:\n\n" + learning + "\n"
    )
    refrences = "## Refrences\n\n* [Title](www.url.com \"Title\")\n\n"
    task_section = (
        "## Tasks\nList of tasks with brief descriptions of each task.\n\n"
    )
    for task in tasks:
        name_number = str(task.number) + ". " + task.name
        task_section += (
            "### [{}]".format(name_number) +
            "(https://github.com/BenDoschGit/holbertonschool-machine_learning/b\
                lob/main/supervised_learning/{}/{}".format(
                project.lower(), task.file
            )
            + "\"{}\")\n\n{}\n\n---\n\n".format(name_number, task.description)
        )

    with open("README.md", "w+") as file:
        text = title + table + learning_objectives + refrences + task_section
        file.write(text)

    file.close()
    return

def main():
    """Main file of module
    """
    
    # Get project title
    project = get_project_title()

    # Create tasks
    tasks = get_tasks()

    # Create learning objectives
    learning = get_leanring_objectives()

    # Create and write to README.md file
    create_readme(project=project, learning=learning, tasks=tasks)

    # Create task files.
    # Code Goes Here

if __name__ == "__main__":
    main()
