from get_py_deps import _cli, get_py_deps


def test_field_names():
    table = get_py_deps("get-py-deps")
    assert table.field_names == ["Package", "License", "Url"]


def test_cli(capsys):
    _cli(["setuptools"])  # Call the CLI function with the desired package name
    captured = capsys.readouterr()  # Capture the printed output

    # Define the expected substrings
    expected_substrings = [
        "Package",
        "License",
        "Url",
    ]

    # Assert that each expected substring is present in the captured output
    for substring in expected_substrings:
        assert substring in captured.out
