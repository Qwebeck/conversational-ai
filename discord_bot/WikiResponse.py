FIRST_LINE = "Results for query: "


class WikiResponse:
    def __init__(self, query, titles, links, status):
        self.query = query
        self.links = links
        self.titles = titles
        self.status = status

    @classmethod
    def empty(cls, status):
        return cls("", "", "", status)

    def __str__(self):
        if self.status == 200:
            if len(self.links) == 0:
                return "No results for chosen query: " + self.query
            result = FIRST_LINE + self.query + "\n"
            for title, link in zip(self.titles, self.links):
                result += title + ':\n ' + link + "\n"
            return result
        return "Request status: \n" + str(self.status)
