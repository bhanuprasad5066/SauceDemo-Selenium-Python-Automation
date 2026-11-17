import pytest

# Apply sanity marker to all tests in this module
pytestmark = pytest.mark.sanity


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce")
    ]
)
def test_login_data(username, password):

    print(
        f"\nUsername: {username}"
    )

    print(
        "Password supplied successfully"
    )

    assert username != ""
    assert password != ""