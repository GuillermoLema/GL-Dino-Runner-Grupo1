
from components.decoration.ornaments.ornament import Ornament


class Heart(Ornament):
    
    def __init__(self, image, pos_x = 50):
        super().__init__(image)
        self.image_rect.y = 500
        self.image_rect.x = pos_x

