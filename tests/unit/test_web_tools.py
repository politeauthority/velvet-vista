"""
    Velvet Vista
    Tests Unit
    Web Tools
    Source: src/velvet-vista/utils/web_tools.py

"""
from velvet_vista.utils import web_tools


class TestUtilsWebTools:

    def test__url_concat(self):
        """Get search field arguments from a url query string.
        :method: api_util._get_search_field_args()
        """
        result = web_tools.url_concat(["https://google.com", "news"])
        expected = "https://google.com/news"
        assert expected == result
        result = web_tools.url_concat(["https://google.com/", "news"])
        assert expected == result

# End File: politeauthority/velvet-vists/tests/test_web_tools.py
