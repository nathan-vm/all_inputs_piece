from domino.testing import piece_dry_run

def test_string_piece():
    input_data = dict(
    input_string  = 'input_string required string.',
    # input_string_optional=""
    input_textarea='input_textarea not required string.',
    input_code="print('Hello world!')",
    input_date="2023-01-01",
    input_time="16:20:00",
    input_datetime="2023-01-01T16:20:00",
    input_enum="option1",
    input_array_string =['Input array to be logged.'],
    input_array_object=[dict(prop1="")]
    )

    output_data = piece_dry_run(
        "StringPiece",
        input_data
    )

    assert output_data["input_string"] is not None
    assert output_data["input_textarea"] is not None
    assert output_data["input_code"] is not None
    assert output_data["input_date"] is not None
    assert output_data["input_time"] is not None
    assert output_data["input_datetime"] is not None
    assert output_data["input_enum"] is not None
    assert output_data["input_array_string"] is not None
    assert output_data["input_array_object"] is not None
