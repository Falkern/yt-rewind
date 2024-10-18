# 🎥 YouTube Rewind

A Python script that summarizes the total length of YouTube videos watched in a specific year based on your YouTube watch history. It uses the YouTube Data API to fetch video durations and provides an easy-to-read summary of your viewing habits. 📊

## 📦 Features

- **Yearly Summarization**: Summarizes video lengths watched in a specified year.
- **Detailed Output**: Displays the total time spent on each YouTuber’s videos, broken down into hours, minutes, and seconds. ⏰
- **Error Handling**: Gracefully manages errors, such as empty JSON files or API errors.

## ⚙️ Requirements

- Python 3.x
- `isodate` library

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Falkern/yt-rewind.git
   cd yt-rewind
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
## 📄 Usage
Obtain your YouTube API key from the [Google Cloud Console](https://console.cloud.google.com).

Export your YouTube watch history from Google Takeout and save it as ```watch-history.json``` in the project directory.

Run the script using the following command:
```bash
python script.py <year> <path_to_watch_history.json> <your_api_key>
```
Replace <year>, <path_to_watch_history.json>, and <your_api_key> with your desired year, the path to your JSON file, and your API key, respectively.

**Example:**
```bash
python script.py 2021 "C:\Users\RickAstley\Documents\GitHub\projects\yt_rewind\watch-history.json" YOUR_API_KEY
```

## 📝 Example Output

```bash
YouTuber Name: 1h 20m 45s
Another YouTuber: 30m 15s
Total Sum: 2h 5m 0s
```

