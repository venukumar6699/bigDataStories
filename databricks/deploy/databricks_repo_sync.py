# Databricks notebook source
import os
import argparse
from databricks.sdk import WorkspaceClient

# COMMAND ----------

def update_databricks_repo(repo_id, branch, host, token):
    """
    Updates the branch of a Databricks repository in a specified workspace.

    Args:
        repo_id (int): The ID of the repository to update.
        branch (str): The name of the branch to set.
        host (str): The Databricks workspace URL.
        token (str): The Databricks personal access token (PAT).
    """
    # Initialize the Databricks client with the specified host and token
    client = WorkspaceClient(host=host, token=token)

    try:
        print(f"Attempting to update repository with ID: {repo_id} to branch: {branch} in workspace: {host}")
        # Update the repository to the specified branch
        client.repos.update(repo_id=repo_id, branch=branch)
        print(f"Successfully updated repository {repo_id} to branch '{branch}' in workspace '{host}'.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {str(e)}")


# COMMAND ----------

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Update Databricks repository branch.")
    parser.add_argument("--repo-id", type=int, required=True, help="The ID of the repository to update.")
    parser.add_argument("--branch", type=str, required=True, help="The name of the branch to set.")
    parser.add_argument("--host", type=str, required=True, help="The Databricks workspace URL.")
    parser.add_argument("--token", type=str, required=True, help="The Databricks personal access token (PAT).")
    args = parser.parse_args()

    update_databricks_repo(args.repo_id, args.branch, args.host, args.token)
