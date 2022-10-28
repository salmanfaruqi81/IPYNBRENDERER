import pytest
from IPYNBRENDERER import get_time_info
from IPYNBRENDERER.custom_exception import InvalidURLException

good_URL_data = [
    ("https://www.youtube.com/watch?v=QJe_B7t2kXg", 0),
    ("https://youtu.be/QJe_B7t2kXg", 0),
    ("https://www.youtube.com/watch?v=QJe_B7t2kXg&t=6s", 6),
]


bad_URL_data = [
    ("https://www.youtube.com/watch?v=QJe_B7t2kXgasd", 0),
    ("https://youtu.be/QJe_B7t2kXgasd", 0),
    ("https://www.youtube.com/watch?v=QJe_B7t2kXg&t=6s", 0),
]


@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response


@pytest.mark.parametrize("URL", bad_URL_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)
