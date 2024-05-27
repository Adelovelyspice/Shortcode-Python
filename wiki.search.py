import wikipedia

def search_wikipedia(query):
    try:
        # Search for the query on Wikipedia
        search_results = wikipedia.search(query)
        
        if not search_results:
            print("No results found.")
            return
        
        # Print the search results
        print("Search results:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result}")
        
        # Get the summary of the first result
        summary = wikipedia.summary(search_results[0])
        print("\nSummary of the top result:")
        print(summary)
    
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation error. The query may refer to multiple topics. Some options are:")
        for option in e.options:
            print(option)
    
    except wikipedia.exceptions.PageError:
        print("Page error. The page does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
query = "Artificial Intelligence"
search_wikipedia(query)