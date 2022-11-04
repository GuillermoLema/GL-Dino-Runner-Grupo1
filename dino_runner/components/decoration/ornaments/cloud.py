
from components.decoration.ornaments.ornament import Ornament


class Cloud(Ornament):
    
    def __init__(self, image):
        super().__init__(image)
        self.image_rect.y = 100

