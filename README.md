# p(retty) commit

## Description

pcommit is a utility that uses AI to generate clear and meaningful commit messages based on your repository changes.
Generated messages follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for better readability and automation.

## Installation

```bash
git clone https://github.com/wannasleeprightnow/pcommit
cd pcommit
pip install -e .
```

## Quick Start
On first launch, you’ll be asked for an API key.
You can generate a free API key at [openrouter](https://openrouter.ai/settings/keys).
Copy and paste your API key into the console when prompted.
Make sure to run pcommit in the root directory of your git repository, or in the directory where you want to generate the commit message.

## Step-by-Step Example

1. **Create a Directory and Navigate to It**  
   Create a new folder for the project and navigate to it:

   ```bash
   mkdir example-repo
   cd example-repo
   ```

2. **Initialize a Git Repository**  
   Initialize an empty Git repository:

   ```bash
   git init
   ```

3. **Create and Add a File**  
   Create a `main.py` file with simple code:

   ```bash
   echo "print('Hello, World!')" >> main.py
   ```

   Stage the file for commit:

   ```bash
   git add main.py
   ```

4. **Check Repository Status**  
   Verify that the file has been staged:

   ```bash
   git status
   ```

   Output:

   ```
   On branch master
   No commits yet
   Changes to be committed:
     (use "git rm --cached <file>..." to unstage)
           new file:   main.py
   ```

5. **Create a Commit with pcommit**  
   Use the `pcommit` utility to automatically generate a commit message:

   ```bash
   pcommit
   ```

   Output confirms the commit with a generated message:

   ```
   [master (root-commit) 8bf4acb] feat: add main.py to output Hello, World!
    1 file changed, 1 insertion(+)
    create mode 100644 main.py
   ```

6. **Check Status After Commit**  
   Ensure the working directory is clean:

   ```bash
   git status
   ```

   Output:

   ```
   On branch master
   nothing to commit, working tree clean
   ```