# Contributing Guide

Thank you for your interest in contributing to the YouTube Content Creation Agent! This document provides guidelines and information for contributors.

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## Getting Started

### Prerequisites

- Python 3.13 or higher
- Git
- UV package manager (recommended)
- API keys for testing (optional)

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/youtube-content-creation-agent.git
   cd youtube-content-creation-agent
   ```

3. **Set up the development environment**
   ```bash
   # Using UV (recommended)
   uv sync

   # Or using pip
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### 1. Choose an Issue

- Check the [Issues](https://github.com/your-repo/issues) page for open tasks
- Comment on the issue to indicate you're working on it
- Create a new issue if you have a feature idea

### 2. Implement Changes

- Write clear, readable code
- Add comments for complex logic
- Follow the existing code style
- Write tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run existing tests
python -m pytest

# Test manually
# Start MCP server
uv run mcp dev mcp_server.py

# Test Flask app
uv run python flask_app.py

# Test Streamlit demo
uv run streamlit run demo.py
```

### 4. Commit Changes

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "feat: add new feature description

- What was changed
- Why it was changed
- Any breaking changes"
```

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create Pull Request on GitHub
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use type hints for function parameters and return values
- Maximum line length: 88 characters (Black formatter default)
- Use descriptive variable and function names

### Code Formatting

This project uses [Black](https://black.readthedocs.io/) for code formatting:

```bash
# Format code
black .

# Check formatting
black --check .
```

### Import Organization

```python
# Standard library imports
import os
import sys

# Third-party imports
import streamlit as st
from dotenv import load_dotenv

# Local imports
from .utils import helper_function
```

### Documentation

- Use docstrings for all public functions and classes
- Follow Google docstring format
- Keep README and docs up to date

Example:
```python
def generate_script(topic: str, style: str = "educational") -> dict:
    """Generate a YouTube video script.

    Args:
        topic: The main topic for the video script.
        style: The style of script (educational, entertainment, news).

    Returns:
        A dictionary containing the script and metadata.

    Raises:
        ValueError: If topic is empty or style is invalid.
    """
```

## Testing

### Unit Tests

- Write tests for all new functions
- Use `pytest` framework
- Place tests in `tests/` directory
- Aim for >80% code coverage

### Manual Testing

- Test all three interfaces (MCP, Flask, Streamlit)
- Verify API key handling
- Test error scenarios
- Check performance with different inputs

## Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No sensitive information committed

### PR Description

Include:
- What changes were made
- Why they were made
- How to test the changes
- Screenshots/videos if UI changes
- Breaking changes (if any)

### Review Process

1. Automated checks run (linting, tests)
2. Code review by maintainers
3. Discussion and feedback
4. Approval and merge

## Types of Contributions

### Bug Fixes

- Fix reported bugs
- Include test case that reproduces the bug
- Verify fix doesn't break existing functionality

### Features

- Discuss feature ideas in Issues first
- Implement incrementally
- Provide comprehensive tests
- Update documentation

### Documentation

- Fix typos and improve clarity
- Add examples and tutorials
- Translate documentation
- Create video tutorials

### Testing

- Write new test cases
- Improve test coverage
- Add integration tests
- Performance testing

## Community

### Communication

- Use GitHub Issues for bugs and features
- Use GitHub Discussions for general questions
- Join our Discord/Slack (if available)

### Recognition

Contributors are recognized through:
- GitHub contributor statistics
- Mention in release notes
- Contributor spotlight (for major contributions)

## License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

## Questions?

If you have questions about contributing:
1. Check existing documentation
2. Search GitHub Issues
3. Ask in GitHub Discussions
4. Contact maintainers directly

Thank you for contributing to the YouTube Content Creation Agent! 🎉