from collections.abc import Iterable


FIRST_LINE = "Results for query: "


class WikiSearchResponse:
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

    @classmethod
    def from_search_response(cls, search_response: str):
        """Parse response from Wikipedia API to WikiSearchResponse object
        :param search_response: response from Wikipedia API formatted as defined by __str__ method of this class"""
        lines = search_response.split('\n')
        query = lines[0].removeprefix(FIRST_LINE)
        titles = [lines[i][:-1] for i in range(1, len(lines[1:]), 2)]
        links = [lines[i].strip() for i in range(2, len(lines[1:]), 2)]
        return cls(query, titles, links, 200)


class WikiRecomendationResponse:
    def __init__(self, most_common_keyphrase: str, occurences: int, search_response: WikiSearchResponse):
        self.most_common_keyphrase = most_common_keyphrase
        self.occurences = occurences
        self.search_response = search_response

    def __str__(self):
        return f"Most common keyphrase from recent articles: {self.most_common_keyphrase} (occured {self.occurences})\n" + str(self.search_response)
