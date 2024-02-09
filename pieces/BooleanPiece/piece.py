from domino.base_piece import BasePiece
from .models import InputModel, OutputModel

class BooleanPiece(BasePiece):
    """
    This Piece serves as a simple example, from where you can start writing your own Piece.
    Remember to also change all other required files accordingly:
    - piece.py (this file)
    - models.py
    - metadata.json
    - requirements.txt or Dockerfile if needed
    """
    
    def piece_function(self, input_data: InputModel):

        self.logger.info("Nothing...")
        self.logger.info(input_data.__dict__)
        output_model_dict = input_data.__dict__
        return OutputModel(
            **output_model_dict,
        )