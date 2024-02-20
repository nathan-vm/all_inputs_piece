from domino.testing import piece_dry_run

def test_date_piece():
    input_data = dict(
    input_date  = '2023-01-01',
    # input_datetime="2023-01-01T16:20:00"
    input_time='16:20:00',
    )

    output_data = piece_dry_run(
        "DatePiece",
        input_data
    )

    assert output_data["input_date"] is not None
    # assert output_data["input_datetime"] is not None
    assert output_data["input_time"] is not None
