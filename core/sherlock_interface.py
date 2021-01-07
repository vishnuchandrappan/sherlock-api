import os
from lib.sherlock.sites import SitesInformation
from lib.sherlock.sherlock import sherlock
from lib.sherlock.result import QueryStatus
from core.custom_notify import QueryNotifyPrint


def parseSherlockResults(username):
    sites = SitesInformation(
        os.path.join(os.path.abspath(__file__ + "/../../"),
                     "lib/sherlock/resources/data.json")
    )

    site_data = {}
    for site in sites:
        site_data[site.name] = site.information

    query_notify = QueryNotifyPrint(result=None)

    results = sherlock(
        username=username,
        site_data=site_data,
        query_notify=query_notify
    )

    responses = []
    for website_name in results:
        dictionary = results[website_name]
        if dictionary.get("status").status == QueryStatus.CLAIMED:
            responses.append(dictionary["url_user"])

    return responses


if __name__ == "__main__":
    print(f'result => {parseSherlockResults("johndoe")}')
