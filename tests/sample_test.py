import pytest
from sampleproject.sampleproject import LikeState, slap_many

# we feed in the names of the parameters for the function we are creating multiple test cases for
@pytest.mark.parametrize("test_input, expected", [
    ("dd", LikeState.empty),
    ("ld", LikeState.disliked),
    ("dl", LikeState.liked),
    ("ldd", LikeState.empty),
    ("lldd", LikeState.empty),
    ("ddl", LikeState.liked),
])
def test_many_slaps(test_input: str, expected: LikeState):
    assert slap_many(LikeState.empty, test_input) is expected
