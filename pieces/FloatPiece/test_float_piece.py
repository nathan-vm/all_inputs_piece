from domino.testing import piece_dry_run

def test_string_piece():
    input_data = dict(
        input_float=1.0,
        input_float_optional=1.0
    )

    output_data = piece_dry_run(
        "FloatPiece",
        input_data
    )

    assert output_data["input_float"] is not None
    assert output_data["input_float_optional"] is not None
