from lib.sherlock.result import QueryStatus


class QueryNotify():

    def __init__(self, result=None):
        self.result = result
        return

    def start(self, message=None):
        return

    def update(self, message=None):
        self.result = result
        return

    def finish(self, message=None):
        return

    def __str__(self):
        result = str(self.result)
        return result


class QueryNotifyPrint(QueryNotify):

    def __init__(self, result=None):
        super().__init__(result)
        return

    def start(self, message):
        title = "Checking username"
        print(f"[*] {title} {message} on:")
        return

    def update(self, result):
        self.result = result

        if self.result.query_time is None:
            response_time_text = ""
        else:
            response_time_text = f" [{round(self.result.query_time * 1000)} ms]"

        # Output to the terminal is desired.
        print(f'[+]{response_time_text} cheking => {self.result.site_name}')
        if result.status == QueryStatus.CLAIMED:
            print(
                f"found: {self.result.site_url_user}")

        return

    def __str__(self):
        result = str(self.result)

        return result
