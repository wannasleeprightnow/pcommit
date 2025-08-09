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