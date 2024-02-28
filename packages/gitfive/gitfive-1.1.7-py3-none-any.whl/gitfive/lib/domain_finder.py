from googlesearch import search
import httpx

import json

from gitfive.lib.objects import GitfiveRunner
from gitfive.lib.utils import extract_domain


def guess_custom_domain(runner: GitfiveRunner):
    company = runner.target.company.lower()

    google = None
    hunter = None

    # Google
    try:
        if company != "google": # googlesearch doesn't return Google.com when searching "google"
            for url in search(company):
                if ("facebook" not in company and "facebook.com" in url) or ("twitter" not in company and "twitter.com" in url) :
                    continue
                google = extract_domain(url)
                break
    except Exception: # https://github.com/mxrch/GitFive/issues/15
        runner.rc.print("[!] Google Search failed, are you using a VPN/Proxy ?", style="italic")

    # Hunter.io
    req = httpx.get(f"https://hunter.io/v2/domains-suggestion?query={company}")
    data = json.loads(req.text)
    if results := data.get("data", [{}]):
        hunter = results[0].get("domain")

    if hunter and (not google or hunter in google):
        runner.rc.print(f'🔍 [Hunter.io] Found possible domain "{hunter}" for company "{company}"', style="light_green")
        return {hunter}
    elif hunter and google:
        runner.rc.print(f'🔍 [Hunter.io] Found possible domain "{hunter}" for company "{company}"', style="light_green")
        runner.rc.print(f'🔍 [Google] Found possible domain "{google}" for company "{company}"', style="light_green")
        return {hunter, google}
    elif google:
        runner.rc.print(f'🔍 [Google] Found possible domain "{google}" for company "{company}"', style="light_green")
        return {google}
    return set()