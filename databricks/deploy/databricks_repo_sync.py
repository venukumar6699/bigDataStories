#databricks notebook source
import os
from databricks.sdk import WorkspaceClient
from databricks.sdk.exceptions import ApiException

def update_repo_branch(repo_id, branch):
    """
    Updates the branch of a Databricks repository.

    Args:
        repo_id (int): The ID of the repository to update.
        branch (str): The name of the branch to set.
    """
    client = WorkspaceClient()

    try:
        print(f"Attempting to update repository with ID: {repo_id} to branch: {branch}")
        client.repos.update(repo_id=repo_id, branch=branch)
        print(f"Successfully updated repository {repo_id} to branch '{branch}'.")
    except ApiException as e:
        # Handle Databricks API errors
        print(f"API Error occurred while updating repository: {e.error_code} - {e.message}")
        if e.error_code == "RESOURCE_DOES_NOT_EXIST":
            print(f"Repository with ID {repo_id} does not exist.")
        elif e.error_code == "INVALID_PARAMETER_VALUE":
            print(f"Invalid parameter provided: {e.message}")
        else:
            print("An unexpected API error occurred.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Get environment variables
    repo_id = os.getenv("REPO_ID")
    branch = os.getenv("BRANCH")

    if not repo_id or not branch:
        print("Environment variables REPO_ID and BRANCH are required.")
        exit(1)

    # Convert repo_id to integer
    try:
        repo_id = int(repo_id)
    except ValueError:
        print("REPO_ID must be an integer.")
        exit(1)

    update_repo_branch(repo_id, branch)
