#!/usr/bin/env python3
"""Module containing functions for creating a README.md file for Holberton
School projects."""

import os
from task import Task


def get_project_info():
    """Takes the current working directory of a holberton project and returns the
    title of the project."""
    directory = os.getcwd()
    temp = directory
    temp = temp.split("\\")
    root_repo = directory.split("GitHub")[-1].split("\\")[1]
    container_repo = directory.split("GitHub")[-1].split("\\")[2:]
    container_repo = "/".join(container_repo)
    title = temp[-1].split("-")[-1].title().replace("-", " ")
    return title, root_repo, container_repo


def get_tasks() -> list:
    """Prompts user for information, then uses it to create objects for each
    task in the project."""
    tasks = []
    go_on = True

    while go_on:
        confirm = ""
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

def create_readme(project, root_repo, container_repo, learning="", tasks=[]) -> None:
    """Takes the project name, learning objectives, and tasks, then
    writes them into the README.md file accoriding to template.

    Args:
        project (str): Name of the project for the README.md file.
        tasks (list, optional): List of tasks for the project. Defaults to [].
        learning (str, optional): Learning objectives for the project. Defaults to "".
    """
    name = "Benjamin Dosch"
    git_hub = "https://github.com/BenDoschGit"
    
    title = "# " + project
    author = "## Author\n\n[{}]({})\n".format(name, git_hub)
    table =  (
        "\n\n1. [Learning Objectives](#learning-objectives)\n2. " +
        "[References](#references)\n3. [Tasks](#tasks)\n" +
        "4. [Author](#author)\n\n"
    )
    count = 0
    for task in tasks:
        count += 1
        table += "\t{}. [{}](#{}-{})\n".format(
                count, task.name, task.number,
                task.name.lower().replace(" ", "-")
            )
    table += "\n4. [Author](#author)\n"
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
            "({}/{}/blob/main/{}/{} ".format(
                git_hub, root_repo, container_repo, task.file
            ) + 
            "\"{}\")\n\n{}\n\n---\n\n".format(name_number, task.description)
        )

    with open("README.md", "w+") as file:
        text = (title + table + learning_objectives + refrences +
                task_section + author)
        file.write(text)

    file.close()
    return

def main():
    """Main file of module
    """
    
    # Get project title
    title, root_repo, container_repo = get_project_info()

    # Create tasks
    tasks = get_tasks()

    # Create learning objectives
    learning = get_leanring_objectives()

    # Create and write to README.md file
    create_readme(project=title, root_repo=root_repo,
                  container_repo=container_repo,learning=learning,
                  tasks=tasks)

    # Create task files.
    for task in tasks:
        with open(task.file, "w+") as file:
            file.close()

if __name__ == "__main__":
    main()
