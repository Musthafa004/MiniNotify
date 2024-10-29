Project Phases :
Phase 1 (MiniNotify) : Initial version with basic notification functionality.
Phase 2 (Mini_notify): Added topic customization and improved UI.
Phase 3 (NewsPopup): Final phase with additional news sources and optimized mini notifications feed.

Project Name :
MiniNotify - Mini_notify - NewsPopup

Project Description :
MiniNotify is a Python-based notification application that fetches the latest news or updates on a given topic and displays them as system notifications. This is especially useful for users who want timely updates directly on their desktop.

Features :
- Fetches news based on specific topics
- Displays notifications with concise headlines and descriptions
- Allows customization of topics for user preference
- Uses `plyer` for cross-platform notification support

Installation :
To run this project locally, you’ll need Python and `plyer` installed. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Musthafa004/MiniNotify.git
Install Required Packages:
bash
Copy code
pip install plyer
Usage
Run the application by executing:

bash
Copy code
python MiniNotify.py
Sample Code Usage
Explain how to modify or use parts of your code, if relevant.

python
Copy code
from MiniNotify import fetch_news, show_notification
fetch_news("Technology")
