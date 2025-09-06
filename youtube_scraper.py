import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm

def get_youtube_service(api_key):
    """Initializes and returns the YouTube API service client."""
    return build('youtube', 'v3', developerKey=api_key)

def fetch_data_for_keywords(api_key, keywords, n_results, max_comments):
    """
    Orchestrates the data fetching process for a list of keywords.
    """
    youtube = get_youtube_service(api_key)
    all_video_data = []

    for keyword in keywords:
        try:
            # 1. Search for top N video IDs
            search_response = youtube.search().list(
                q=keyword, part='id', type='video', maxResults=n_results
            ).execute()
            video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]

            if not video_ids: continue

            # 2. Get video details (views, likes, etc.) in a single batch call
            video_details_response = youtube.videos().list(
                part='snippet,statistics', id=','.join(video_ids)
            ).execute()

            # 3. Fetch comments for each video and combine data
            for item in video_details_response.get('items', []):
                video_id = item['id']
                snippet = item['snippet']
                stats = item.get('statistics', {})
                comments = []
                try:
                    comment_response = youtube.commentThreads().list(
                        part='snippet', videoId=video_id, maxResults=max_comments, textFormat='plainText'
                    ).execute()
                    comments = [c['snippet']['topLevelComment']['snippet']['textDisplay'] for c in comment_response.get('items', [])]
                except HttpError:
                    pass # Silently ignore if comments are disabled

                video_data = {
                    'keyword': keyword,
                    'video_id': video_id,
                    'title': snippet['title'],
                    'description': snippet['description'],
                    'views': int(stats.get('viewCount', 0)),
                    'likes': int(stats.get('likeCount', 0)),
                    'comment_count': int(stats.get('commentCount', 0)),
                    'comments': comments
                }
                all_video_data.append(video_data)
        except HttpError as e:
            print(f"An HTTP error occurred: {e}")
            break
            
    return pd.DataFrame(all_video_data)