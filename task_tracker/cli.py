# task_tracker/cli.py
import click
from task_tracker.models import User, Project, Task, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URI = 'sqlite:///task_tracker/tasks.db'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)  # Create tables if not exist
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--username', prompt='Enter username', help='User\'s username')
def add_user(username):
    new_user = User(username=username)
    session.add(new_user)
    session.commit()
    click.echo(f'User {username} added successfully.')

@cli.command()
@click.option('--name', prompt='Enter project name', help='Project name')
def add_project(name):
    new_project = Project(name=name)
    session.add(new_project)
    session.commit()
    click.echo(f'Project {name} added successfully.')

@cli.command()
@click.option('--description', prompt='Enter task description', help='Task description')
@click.option('--user_id', prompt='Enter user ID', help='User ID')
@click.option('--project_id', prompt='Enter project ID', help='Project ID')
def add_task(description, user_id, project_id):
    new_task = Task(
        description=description,
        user_id=user_id,
        project_id=project_id,
        created_at=datetime.utcnow()
    )
    session.add(new_task)
    session.commit()
    click.echo(f'Task "{description}" added successfully.')

if __name__ == '__main__':
    cli()
