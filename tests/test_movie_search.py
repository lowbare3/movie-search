import unittest
from movie_search import search_movies

class TestMovieSearch(unittest.TestCase):

    def test_output_type(self):
        """Check if the function returns a DataFrame"""
        result = search_movies("spy thriller in Paris", top_n=3)
        self.assertTrue(hasattr(result, "iloc"))  # DataFrame check

    def test_top_n(self):
        """Check if the function returns exactly top_n results"""
        result = search_movies("spy thriller in Paris", top_n=3)
        self.assertEqual(len(result), 3)

    def test_similarity(self):
        """Check if different queries give different results"""
        result1 = search_movies("spy thriller in Paris", top_n=1)
        result2 = search_movies("romantic comedy", top_n=1)
        self.assertNotEqual(result1.iloc[0]["title"], result2.iloc[0]["title"])

    def test_relevance(self):
        """Check if query text is somewhat relevant to returned plots"""
        query = "spy thriller in Paris"
        result = search_movies(query, top_n=3)

        # At least one of the returned plots should contain a related keyword
        relevance_keywords = ["spy", "thriller", "paris"]
        found_relevance = any(
            any(keyword.lower() in str(plot).lower() for keyword in relevance_keywords)
            for plot in result["plot"]
        )
        self.assertTrue(found_relevance, "Results are not relevant to the query")

if __name__ == "__main__":
    unittest.main()
