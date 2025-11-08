# YouTube Video Uploader with Scheduled Publishing

This Python script allows you to **upload videos to YouTube** and optionally **schedule them for future publishing** using the YouTube Data API v3.

---

## Features

- Upload videos directly from your local machine.
- Schedule videos to be published at a specific date and time.
- Add metadata: title, description, tags, and category.
- Automatically handles OAuth2 authentication with Google.

---

## Prerequisites

1. **Python 3.7+**
2. Install required Python packages:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

3. **Google API credentials**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a project and enable the **YouTube Data API v3**.
   - Create **OAuth 2.0 Client ID** credentials.
   - Download the JSON file and save it as `YOUR_SECRET_FILE.json`.

---

## Usage

1. **Update script constants**:

```python
CLIENT_SECRETS_FILE = "YOUR_SECRET_FILE.json"  # Path to your credentials
```

2. **Call the `upload_video` function** with your video details:

```python
import datetime
from uploader import upload_video  # if saved as uploader.py

target_time = datetime.datetime(2025, 11, 10, 15, 30)  # local time

upload_video(
    file_path="my_video.mp4",
    title="My Scheduled Short",
    description="Uploaded automatically, scheduled publish!",
    tags=["gaming", "shorts"],
    publish_datetime=target_time
)
```

- `file_path`: Path to your local video file.
- `title`: Video title.
- `description`: Video description.
- `tags`: Optional list of tags.
- `category_id`: YouTube category ID (default is `22` for "People & Blogs").
- `publish_datetime`: Optional `datetime` object to schedule publishing.

3. **Run the script**:

```bash
python uploader.py
```

The script will open a browser window for Google OAuth authentication the first time.

---

## Notes

- Scheduled videos must have `privacyStatus` set to `"private"`; YouTube will automatically make them public at the scheduled time.
- All timestamps are converted to UTC before sending to YouTube.

---

## References

- [YouTube Data API v3](https://developers.google.com/youtube/v3)
- [Google API Python Client](https://github.com/googleapis/google-api-python-client)
- [OAuth 2.0 for Installed Applications](https://developers.google.com/identity/protocols/oauth2)

---

## License

No License

