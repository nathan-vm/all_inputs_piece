from domino.testing import piece_dry_run

def test_string_piece():
    input_data = dict(
    input_boolean=False,
    input_boolean_optional=True,
    input_array_boolean=[False,False,True],
    input_array_object=[dict(prop1=True)],
    )

    output_data = piece_dry_run(
        "BooleanPiece",
        input_data
    )

    assert output_data["input_boolean"] is not None
    assert output_data["input_boolean_optional"] is not None
    assert output_data["input_array_boolean"] is not None
    assert output_data["input_array_object"] is not None
