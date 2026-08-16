# Git Helpers

A collection of convenient utilities to simplify common Git operations (push and pull) with interactive user confirmations and error handling.

## Overview

Git Helpers provides a set of tools that make it easier to manage Git repositories without needing to remember complex Git commands. This project includes both **GUI-based Python scripts** and **command-line batch scripts** for Windows environments.

The tools offer:
- 🎯 Simple push and pull operations with user confirmations
- ⚠️ Error handling with automatic retry options
- 💪 Force push/pull capability as fallback options
- 🖥️ Both GUI (Python) and CLI (Batch) interfaces

## Files

### Push Operations
- **`Push.pyw`** - Python GUI application for pushing changes
  - Enter commit message via GUI dialog
  - Adds all changes (`git add .`)
  - Commits with your message
  - Pushes to remote with force option if needed
  
- **`Push.bat`** - Command-line batch script for pushing changes
  - Interactive command-line prompts
  - Same workflow as Push.pyw but without GUI
  - Useful for automation and server environments

### Pull Operations
- **`Pull.pyw`** - Python GUI application for pulling changes
  - Simple confirmation dialog
  - Pulls latest changes from remote
  - Offers force pull option on failure
  
- **`Pull.bat`** - Command-line batch script for pulling changes
  - Interactive command-line prompts
  - Same workflow as Pull.pyw but without GUI

### Utilities
- **`Create exe.bat`** - Build script to compile Python scripts into standalone .exe files
  - Uses PyInstaller to create Windows executables
  - Generates `Pull.exe` and `Push.exe`
  - Cleans up temporary build files automatically
  - Pre-built executables (`Pull.exe`, `Push.exe`) are included in the repository

## Requirements

### For Python Scripts (.pyw)
- Python 3.6+
- Git installed and accessible from command line

### For Batch Scripts (.bat)
- Windows OS
- Git installed and accessible from command line

### For Building Executables
- Python 3.6+
- PyInstaller: `pip install pyinstaller`
- Git installed

## Usage

### Using Python GUI Scripts

1. **Push changes:**
   ```bash
   python Push.pyw
   ```
   - Enter your commit message in the dialog
   - Confirm the commit and push
   - If push fails, you'll be offered a force push option

2. **Pull changes:**
   ```bash
   python Pull.pyw
   ```
   - Confirm the pull operation
   - If pull fails, you'll be offered a force pull option

### Using Batch Scripts

1. **Push changes:**
   ```bash
   Push.bat
   ```
   - Enter commit message when prompted
   - Confirm the operation
   - Optional force push if standard push fails

2. **Pull changes:**
   ```bash
   Pull.bat
   ```
   - Confirm the pull operation
   - Optional force pull if standard pull fails

### Using Pre-built Executables

Simply double-click or run from command line:
- `Pull.exe` - Run pull operation with GUI
- `Push.exe` - Run push operation with GUI

### Building Executables

To create Windows .exe files from the Python scripts:

```bash
Create exe.bat
```

This will:
- Compile `Pull.pyw` → `Pull.exe`
- Compile `Push.pyw` → `Push.exe`
- Clean up temporary build files

## Features

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

Both tools include robust error handling:
- **Validation**: Ensures commit messages aren't empty and operations are intentional
- **Fallback Options**: Offers force operations (push --force, pull --force) when standard operations fail
- **User Feedback**: Clear success and error messages via dialogs or console output
- **Exit Safety**: Gracefully handles failures without leaving repository in inconsistent state

## Notes

⚠️ **Warning**: Force push and force pull are powerful operations that can overwrite changes. Use with caution!

- Force push may overwrite remote changes
- Force pull may discard local changes
- Always ensure you have backups if using force operations on shared repositories

## License

This project is provided as-is for personal and educational use.

## Contributing

Feel free to suggest improvements or modifications to these helper tools.

---

**Created by:** Yan-519  
**Language:** Python (54%) & Batch (46%)
