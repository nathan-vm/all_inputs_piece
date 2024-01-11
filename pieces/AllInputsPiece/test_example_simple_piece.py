from domino.testing import piece_dry_run

def test_example_simple_piece():
    input_data = dict(
        input_string="default value",
        input_code = "print('Hello world!')",
        input_date="2023-01-01",
        input_time="16:20:00",
        input_datetime="2023-01-01T16:20:00",
        input_integer=10,
        input_float=10.5,
        input_float2=0.1,
        input_boolean=False,
        input_enum="option1",
        input_all_required=1,
        input_all=1,
        input_array_string=["default_1", "default_2", "default_3"],
        input_array_float=[10.1, 10.2, 10.3],
        input_array_float_2=[10.1, 10.2, 10.3],
        input_array_integer=[10 , 10 , 10 ],
        input_array_all_required=["string",1],
        input_array_object=[
            dict(prop1="",prop2=1)
        ]
    )

    output_data = piece_dry_run(
        "AllInputsPiece",
        input_data
    )

    assert output_data["message"] is not None
