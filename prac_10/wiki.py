"""
CP1404 prac_10 Wikipedia program
Estimated time: 1 hour
Actual time: 50 minutes
"""

import wikipedia


def main():
    print("Wikipedia Search")
    search_title = input("Enter page title: ").strip()

    while search_title != "":
        try:
            page = wikipedia.page(search_title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(error.options)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_title}" does not match any pages. Try another id!')

        except Exception as error:
            print(f"An unexpected error occurred: {error}")

        print()
        search_title = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
