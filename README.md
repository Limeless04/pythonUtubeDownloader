# Python YouTube Downloader

A simple Python YouTube downloader built with PySide6 and Pytube.

## Version 0.1

### Features

- Download videos from YouTube.
- Preview videos.
- Progress bar.

## Version 0.1.5

### Features

- Added the ability to select the destination folder for saving the downloaded video.
- Implemented placeholders for URL and folder path inputs.

## Version 0.2

In this version, the code has been refactored to adhere more closely to object-oriented programming principles. The code has been split into different classes for improved organization and ease of maintenance.

### Features

No new features have been added in this version; only code refactoring has been performed.

### Issues to Fix

- Performance issue: The application takes a long time to load the preview after pasting the URL. 
  - Proposed solutions:
    - Implement threading to handle the preview in a separate thread to avoid interrupting the UI.
    - Utilize async/await in Python.
    - Consider implementing caching using Redis or SQLAlchemy.

### Notes

- Improve error handling in the code.
- Refine if-else statements for better readability and maintainability.
