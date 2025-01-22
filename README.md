# Steam Screenshot Downloader Guide

## Overview
This script automates the process of downloading Steam user screenshots from a specific game's community page. It utilizes Selenium to scroll through the page and BeautifulSoup to extract and download the images.

## Prerequisites

Ensure you have the following installed before running the script:

- Python (>= 3.7)
- Required Python packages:
  ```bash
  pip install requests beautifulsoup4 selenium webdriver-manager lxml
  ```
- Google Chrome installed (latest version)
- Chrome WebDriver (automatically managed by `webdriver-manager`)

## Script Configuration

Edit the following variables at the beginning of the script to customize its behavior:

- `project_name`: Name of the project (used for naming the folder where screenshots will be saved). Example:
  ```python
  project_name = "Police"
  ```
  Resulting folder: `SteamScreenshotsPolice`

- `appid`: The Steam App ID of the game you want to fetch screenshots from. Example:
  ```python
  appid = "997010"
  ```

- `approx_screenshots`: Approximate number of screenshots to download. Each scroll loads around 12 images, so the script calculates the required scrolls automatically. Example:
  ```python
  approx_screenshots = 24  # Downloads ~24 screenshots with 2 scrolls
  ```

## How to Run the Script

1. Save the script as `steam_screenshot_downloader.py`.
2. Open a terminal and navigate to the script's directory.
3. Run the script using:
   ```bash
   python steam_screenshot_downloader.py
   ```

## Expected Output

The script will perform the following actions:

1. Open the Steam screenshots page for the specified game.
2. Scroll the page to load more screenshots (based on your input).
3. Parse and download available screenshots.
4. Save the images in the specified folder (e.g., `SteamScreenshotsPolice`).

Upon completion, you will see output indicating the number of screenshots found and their download status.

## Troubleshooting

- **No screenshots downloaded:** Ensure the app ID is correct and the community page contains public screenshots.
- **ChromeDriver issues:** Update Chrome or manually install the appropriate version of ChromeDriver.
- **Network issues:** Ensure you have a stable internet connection.

## Future Improvements

- Adding support for command-line arguments to specify settings.
- Enhancing error handling and logging features.

---

Enjoy downloading your Steam screenshots efficiently!
