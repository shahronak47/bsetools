from google import google
import pdb

if __name__ == '__main__' :
    search_results = google.search("dolphin offshore share price")
    for result in search_results :
        print(result.link)