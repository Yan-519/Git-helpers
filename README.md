# Git Helpers

A collection of convenient utilities to simplify common Git operations (push and pull) with interactive user confirmations and error handling.

## Overview

Git Helpers provides a set of tools that make it easier to manage Git repositories without needing to remember complex Git commands. This project includes both **GUI-based Python scripts** and **command-line batch scripts**.

The tools offer:
- 🎯 Simple push and pull operations with user confirmations
- ⚠️ Error handling with automatic retry options
- 💪 Force push/pull capability as fallback options

## Files

### Commit Operations **`local commit.bat`**
  - Command-line batch script for staging and committing changes
  - Checks for uncommitted changes before proceeding
  - Validates commit message is not empty
  - Interactive command-line prompts with confirmation
  - Useful for local commits before pushing

### Push Operations **`Push.bat`**
  - Command-line batch script for pushing changes
  - Interactive command-line prompts
  - Same workflow as Push.pyw but without GUI
  - Useful for automation and server environments

### Pull Operations **`Pull.bat`**
  - Command-line batch script for pulling changes
  - Interactive command-line prompts
  - Same workflow as Pull.pyw but without GUI

## Requirements (For Batch Scripts [.bat])
- Windows OS
- Git installed and accessible from command line

## Using Batch Scripts

1. **Commit changes:**
   ```bash
   local commit.bat
   ```
   - Script checks for uncommitted changes
   - Enter commit message when prompted
   - Confirm the operation
   - Changes are staged and committed

2. **Push changes:**
   ```bash
   Push.bat
   ```
   - Enter commit message when prompted
   - Confirm the operation
   - Optional force push if standard push fails

3. **Pull changes:**
   ```bash
   Pull.bat
   ```
   - Confirm the pull operation
   - Optional force pull if standard pull fails

## Features

### Commit Workflow
1. Checks for uncommitted changes using `git status --porcelain`
2. Exits early if no changes found
3. Prompts for commit message
4. Validates that message is not empty
5. Asks for confirmation before proceeding
6. Stages all changes (`git add .`)
7. Creates commit with your message
8. Shows success/error messages

### Push Workflow
1. Opens GUI dialog for commit message input
2. Validates that message is not empty
3. Asks for confirmation before proceeding
4. Stages all changes (`git add .`)
5. Creates commit with your message
6. Pushes to remote repository
7. If push fails, offers force push as alternative

### Pull Workflow
1. Asks for confirmation before pulling
2. Attempts standard pull
3. If pull fails, offers force pull option
4. Shows success/error messages

## Error Handling

All tools include robust error handling:
- **Validation**: Ensures commit messages aren't empty and operations are intentional
- **Change Detection**: Checks for uncommitted changes before attempting operations
- **Fallback Options**: Offers force operations (push --force, pull --force) when standard operations fail
- **User Feedback**: Clear success and error messages via dialogs or console output
- **Exit Safety**: Gracefully handles failures without leaving repository in inconsistent state

## Notes

⚠️ **Warning**: Force push and force pull are powerful operations that can overwrite changes. Use with caution!

- Force push may overwrite remote changes
- Force pull may discard local changes
- Always ensure you have backups if using force operations on shared repositories

## Contributing

Feel free to suggest improvements or modifications to these helper tools.

---

**Created by:** Yan-519  
**Language:** Batch (100%)
