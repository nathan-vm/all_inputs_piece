from domino.testing import piece_dry_run

def test_integer_piece():
    input_data = dict(
        input_integer=1,
        input_integer_optional=1
    )

    output_data = piece_dry_run(
        "IntegerPiece",
        input_data
    )

    assert output_data["input_integer"] is not None
    assert output_data["input_integer_optional"] is not None
