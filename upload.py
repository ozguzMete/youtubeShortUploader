import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import google_auth_oauthlib.flow

# OAuth credentials
CLIENT_SECRETS_FILE = "YOUR_SECRET_FILE.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES
    )
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)


def upload_video(file_path, title, description, tags=None, category_id="22", publish_datetime=None):
    youtube = get_authenticated_service()

    # Convert local time to UTC RFC3339
    if publish_datetime:
        publish_time = publish_datetime.astimezone(datetime.timezone.utc).isoformat()
    else:
        publish_time = None

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": "private",  # must be private for scheduled publishing
            "publishAt": publish_time
        }
    }

    media = MediaFileUpload(file_path)
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = request.execute()
    print(f"✅ Uploaded! Video ID: {response['id']}")
    if publish_time:
        print(f"⏰ Scheduled to go public at {publish_time}")

if __name__ == "__main__":
    # Example: schedule for 8 Nov 2025 at 15:30 local time
    target = datetime.datetime(2025, 11, 10, 15, 30)  # your local time

    upload_video(
        file_path="#cprv2077-#Cyberpunk2077-2-V.mp4",
        title="My Scheduled Short",
        description="Uploaded automatically, scheduled publish!",
        tags=["gaming", "shorts"],
        publish_datetime=target
    )

