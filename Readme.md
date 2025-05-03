# ews-mail-automation

A Python package for secure automation and interaction with Microsoft Exchange servers via EWS (Exchange Web Services). 
Designed to support CLI-based operations for rule management, folder handling, and mail processing, with future extensibility for integration with LLM-powered email assistants.

## ✨ Features

- 🔐 **Authentication**
  - Supports secure login with AD credentials (via EWS)
  - Credential input via CLI, environment variables, or session profile
  - Persists session locally for secure re-use (without re-entering credentials)

- 🧠 **Rules & Folders**
  - Fetch and export mailbox rules (YAML or JSON formats)
  - CRUD operations for folders

- ✉️ **Mail Operations**
  - List, delete, copy, and move emails between folders

- 🖥️ **Command Line Interface**
  - Modular CLI built with `argparse` and subcommands
  - Auto help docs for each subcommand
  - Supports interactive `login`, rule exports, folder and mail commands

- ✅ **Testing & TDD**
  - Test-driven development (TDD) approach with comprehensive unit tests using `pytest`
  - Mocks used to isolate Exchange dependency for fast, offline testing

- 🔁 **CI/CD**
  - GitHub Actions to run tests (via `pytest` and `tox`)
  - Will publish to PyPI once stable

## 🔧 Installation

```bash
pip install ews-mail-automation
```
