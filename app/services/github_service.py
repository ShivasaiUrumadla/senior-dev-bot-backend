from app.config import GITHUB_PAT
import requests


def get_pr_diff(repo, pr_number, installation_token):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"

    headers = {
        "Accept": "application/vnd.github.v3.diff",
        "Authorization": f"Bearer {installation_token}"
    }

    print("inside get_diff()")

    response = requests.get(url, headers=headers)
    response.raise_for_status()


    
    return response.text

def comment(review,repo_name,pr_number,installation_token):

    url=f"https://api.github.com/repos/{repo_name}/issues/{pr_number}/comments"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {installation_token}"
    }
    
    response=requests.post(url=url,headers=headers,json={"body": review})

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    return {
        "status": response.status_code,
        "response": response.text
    }
    # return response.json()











def get_pr_context(repo: str, pr_number: int, token: str, ref: str):
    changed_files = get_changed_files(
        repo=repo,
        pr_number=pr_number,
        token=token
    )

    files = []

    for file in changed_files:
        file_path = file["filename"]

        # We only want actual source files for now.
        if file["status"] == "removed":
            continue

        content = get_file_content(
            repo=repo,
            file_path=file_path,
            token=token,
            ref=ref
        )

        files.append({
            "path": file_path,
            "content": content
        })

    return {
        "files": files
    }



def get_file_content(repo: str, file_path: str, token: str, ref: str):
    url = f"https://api.github.com/repos/{repo}/contents/{file_path}"

    headers = {
        "Accept": "application/vnd.github.raw+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2026-03-10"
    }

    params = {
        "ref": ref
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    return response.text


def get_changed_files(repo: str, pr_number: int, token: str):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2026-03-10"
    }

    response = requests.get(
        url,
        headers=headers
    )

    response.raise_for_status()

    return response.json()



def get_repository_files(repo: str, token: str, ref: str):
    url = f"https://api.github.com/repos/{repo}/git/trees/{ref}"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2026-03-10"
    }

    params = {
        "recursive": "1"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    response.raise_for_status()


    tree = response.json()["tree"]
    print("Total tree items:", len(tree))
    files = []
    SOURCE_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".jsx",
        ".tsx",
        ".java",
        ".cpp",
        ".c",
        ".h",
        ".hpp",
        ".go",
        ".rs",
    }

    source_file_count = 0

    for item in tree:
        if item["type"] != "blob":
            continue

        file_path = item["path"]

        if not any(file_path.endswith(ext) for ext in SOURCE_EXTENSIONS):
            continue

        source_file_count += 1
        content = get_file_content(
            repo=repo,
            file_path=file_path,
            token=token,
            ref=ref
        )

        files.append({
            "path": file_path,
            "content": content
        })
    print("Source files to ingest:", source_file_count)

    return files

def build_retrieval_query(diff: str):
    current_file = None
    changed_lines = []

    for line in diff.splitlines():

        if line.startswith("+++ b/"):
            current_file = line[6:]

        if (line.startswith("+") or line.startswith("-")) \
                and not line.startswith("+++") \
                and not line.startswith("---"):

            changed_lines.append(line)

    return f"""
File: {current_file}

Changed code:
{chr(10).join(changed_lines)}
"""
