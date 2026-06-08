from langchain_community.tools import (
    DuckDuckGoSearchRun
)

from langchain_community.tools import (
    WikipediaQueryRun
)

from langchain_community.utilities import (
    WikipediaAPIWrapper
)

# Wikipedia

wiki = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper()
)

print("\nWikipedia:")
print(
    wiki.invoke("Artificial Intelligence")
)

# Search

search = DuckDuckGoSearchRun()

print("\nSearch:")
print(
    search.invoke(
        "Latest AI Trends"
    )
)

# Calculator

print("\nCalculator:")
print(eval("25 * 8 + 10"))