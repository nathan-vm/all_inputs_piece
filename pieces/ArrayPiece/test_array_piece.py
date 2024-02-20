from domino.testing import piece_dry_run

def test_array_piece():
    input_data = dict(
        input_array_string=['input_string required string.'],
        input_array_object=[]
    )

    output_data = piece_dry_run(
        "ArrayPiece",
        input_data
    )

    assert output_data["input_array_string"] is not None
    assert output_data["input_array_object"] is not None
