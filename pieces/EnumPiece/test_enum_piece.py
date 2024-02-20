from domino.testing import piece_dry_run

def test_enum_piece():
    input_data = dict(
        input_enum_string='option1',
        input_enum_int=1,
        input_enum_float=30.3,
    )

    output_data = piece_dry_run(
        "EnumPiece",
        input_data
    )

    assert output_data["input_enum_string"] is not None
    assert output_data["input_enum_int"] is not None
    assert output_data["input_enum_float"] is not None
