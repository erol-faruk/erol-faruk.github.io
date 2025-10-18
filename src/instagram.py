import importlib
from utils import rate_limited

@rate_limited(0.5)
def lookup_instagram(username: str, config: dict = None) -> str:
    config = config or {}
    use_instaloader = config.get("instagram", {}).get("use_instaloader", True)
    if not use_instaloader:
        return "[INFO] Instagram lookup disabled in config."
    try:
        instaloader = importlib.import_module("instaloader")
    except ModuleNotFoundError:
        return "[ERROR] instaloader not installed. Install with: pip install instaloader"
    L = instaloader.Instaloader(download_pictures=False, download_videos=False)
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        parts = [
            f"Username: {profile.username}",
            f"Full name: {profile.full_name}",
            f"Bio: {profile.biography}",
            f"Is private: {profile.is_private}",
            f"Followers: {profile.followers}",
            f"Profile pic URL: {profile.profile_pic_url}",
        ]
        return "\\n".join(parts)
    except Exception as e:
        return f"[ERROR] Could not fetch profile: {e}"
