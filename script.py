import json
import urllib.request
from datetime import datetime
import isodate
import sys


def check_year(time, year):
    try:
        date_to_check = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        date_to_check = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")

    return date_to_check.year == year


def get_video_length(url, api_key):
    try:
        temp = url.split('?v=')
        video_id = temp[-1]
        search_url = (
            f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=contentDetails"
        )
        response = urllib.request.urlopen(search_url).read()
        data = json.loads(response)
        all_data = data.get("items", [])

        if not all_data:
            print(f"No data found for video ID: {video_id}")
            return 0

        content_details = all_data[0].get("contentDetails", {})
        duration = content_details.get("duration", "")
        duration = isodate.parse_duration(duration)
        return duration.total_seconds()
    
    except (urllib.error.HTTPError, KeyError, json.JSONDecodeError) as e:
        print(f"Error fetching video length for {url}: {e}")
        return 0


def summarize_video_lengths(data, year, api_key):
    results = {}
    
    for video in data:
        url = video.get("titleUrl")
        if url and check_year(video["time"], year):
            if "subtitles" in video:
                youtuber = video["subtitles"][0]["name"]
                video_length = get_video_length(url, api_key)
                results[youtuber] = results.get(youtuber, 0) + video_length

    return results


def main(year, file_path, api_key):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not data:
                print("Error reading JSON file: JSON file is empty.")
                return
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return

    results = summarize_video_lengths(data, year, api_key)
    
    if not results:
        print("No video data found for the specified year.")
        return

    top = sorted(results.items(), key=lambda x: x[1], reverse=True)
    for v, length in top:
        print(f"{v}: {length // 3600}h {(length % 3600) // 60}m {length % 60}s")
    
    total_sum = sum(length for _, length in top)
    print(f"Total Sum: {total_sum // 3600}h {(total_sum % 3600) // 60}m {total_sum % 60}s")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <year> <path_to_watch_history.json> <api_key>")
        sys.exit(1)

    year_input = int(sys.argv[1])
    file_path_input = sys.argv[2]
    api_key_input = sys.argv[3]

    main(year_input, file_path_input, api_key_input)
