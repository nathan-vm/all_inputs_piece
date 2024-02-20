from domino.testing import piece_dry_run

def test_string_piece():
    input_data = dict(
        input_boolean=True,
    )

    output_data = piece_dry_run(
        "BooleanPiece",
        input_data
    )

    assert output_data["input_boolean"] is not None
