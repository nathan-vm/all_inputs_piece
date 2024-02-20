from domino.testing import piece_dry_run

def test_string_piece():
    input_data = dict(
        input_string  = 'input_string required string.',
        input_string_optional="",
        input_textarea='input_textarea not required string.',
        input_code="print('Hello world!')",
    )

    output_data = piece_dry_run(
        "StringPiece",
        input_data
    )

    assert output_data["input_string"] is not None
    assert output_data["input_string_optional"] is not None
    assert output_data["input_textarea"] is not None
    assert output_data["input_code"] is not None
