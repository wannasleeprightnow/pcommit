import json
import pathlib
import subprocess
import urllib.request

AI_SYSTEM_PROMPT = """You are an AI assistant that generates concise and clear commit messages following the Conventional Commits specification.
    You will receive a git diff as input.
    Your task is to analyze the changes and generate a single commit message that accurately summarizes the main purpose of the changes, using the correct Conventional Commits format.
    Instructions:

    Use one of the following types: feat, fix, docs, style, refactor, perf, test, chore, or build.
    Write a short, imperative summary in the subject line (max 72 characters).
    Do not include any unrelated information or explanations.
    Your response must contain only the commit message itself. Do not include any explanations, greetings, or additional text.
    Input:
    A git diff representing the changes to be committed.

    Output:
    A single commit message in the Conventional Commits format, summarizing the changes in the provided git diff.
    """


class ConfigDoesntExistsError(BaseException): ...


def read_config() -> str:
    config_path = pathlib.Path(pathlib.Path.home() / ".config" / "pcommit")
    if config_path.exists():
        with open(config_path, "r") as file:
            api_key = file.readline().split("=")[1].strip("\n")
            return api_key
    else:
        raise ConfigDoesntExistsError


def get_new_api_key() -> str:
    api_key = input(
        "Your api key was not found. Please generate it from the link https://openrouter.ai/settings/keys and paste it here:\n"
    )
    config_path = pathlib.Path(pathlib.Path.home() / ".config" / "pcommit")
    with open(config_path, "w") as file:
        file.write(f"API_KEY={api_key}")
    subprocess.run(["chmod", "600", config_path])
    return api_key


def get_git_diff() -> str:
    diff_without_index = subprocess.run(["git", "diff"], text=True, capture_output=True).stdout
    if diff_without_index:
        return diff_without_index
    return subprocess.run(["git", "diff", "--cached"], text=True, capture_output=True).stdout


def get_commit_message(git_diff_text: str, api_key: str) -> str | dict:
    
    req = urllib.request.Request(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        data=json.dumps(
            {
                "model": "openai/gpt-oss-20b:free",
                "messages": [
                    {
                        "role": "system",
                        "content": AI_SYSTEM_PROMPT,
                    },
                    {"role": "user", "content": git_diff_text},
                ],
            }
        ).encode('utf-8'),
    )
    
    with urllib.request.urlopen(req) as response:
        response_data = json.loads(response.read().decode('utf-8'))
    
    return (
        dict(response_data)
        .get("choices", [""])[0]
        .get("message", {})
        .get("content", {})
    )


def main():
    try:
        api_key = read_config()
    except ConfigDoesntExistsError:
        api_key = get_new_api_key()
    git_diff_text = get_git_diff()
    if git_diff_text:
        commit_message = get_commit_message(git_diff_text, api_key)
        subprocess.run(["git", "commit", "-a", "-m", commit_message])
    else:
        print("Nothing to commit!")
        exit()

if __name__ == "__main__":
    main()
