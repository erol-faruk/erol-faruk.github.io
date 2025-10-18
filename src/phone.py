import phonenumbers
from phonenumbers import geocoder, carrier, timezone as tz
from utils import rate_limited

@rate_limited(0.5)
def lookup_phone(number: str, config: dict = None) -> str:
    config = config or {}
    try:
        pn = phonenumbers.parse(number, None)
    except Exception as e:
        return f"[ERROR] Could not parse number: {e}"
    out = {
        'valid': phonenumbers.is_valid_number(pn),
        'possible': phonenumbers.is_possible_number(pn),
        'e164': phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164),
        'country': geocoder.description_for_number(pn, "en"),
        'carrier': carrier.name_for_number(pn, "en"),
        'timezones': tz.time_zones_for_number(pn)
    }
    lines = [f"Number: {out.get('e164')}",
             f"Valid: {out.get('valid')}  Possible: {out.get('possible')}",
             f"Country: {out.get('country')}",
             f"Carrier: {out.get('carrier')}",
             f"Timezones: {', '.join(out.get('timezones') or [])}"]
    return "\\n".join(lines)
