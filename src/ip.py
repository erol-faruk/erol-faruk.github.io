import requests
from utils import rate_limited
IP_API_URL = "http://ip-api.com/json/{ip}"

@rate_limited(0.5)
def lookup_ip(ip: str, config: dict = None) -> str:
    try:
        resp = requests.get(IP_API_URL.format(ip=ip), timeout=8)
        if resp.ok:
            data = resp.json()
            if data.get("status") == "success":
                parts = [
                    f"IP: {ip}",
                    f"Country: {data.get('country')} ({data.get('countryCode')})",
                    f"Region: {data.get('regionName')} - {data.get('city')}",
                    f"ISP: {data.get('isp')}",
                    f"Org: {data.get('org')}",
                    f"Lat/Lon: {data.get('lat')}/{data.get('lon')}",
                    f"Timezone: {data.get('timezone')}",
                ]
                return "\\n".join(parts)
    except Exception:
        pass
    return "[ERROR] All providers failed or returned no data."
