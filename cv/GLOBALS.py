from typing import Tuple

# standard image sizes
STD_IMG_SIZE: int = 256
STD_IMG_TUPLE: Tuple = (STD_IMG_SIZE, STD_IMG_SIZE)
STD_IMG_TUPLE_SINGLE: Tuple = (STD_IMG_SIZE, STD_IMG_SIZE, 1)
STD_IMG_TUPLE_MULTI: Tuple = (STD_IMG_SIZE, STD_IMG_SIZE, 3)

STD_IMG_TUPLE_SINGLE_TORCH: Tuple = (1, STD_IMG_SIZE, STD_IMG_SIZE)
STD_IMG_TUPLE_MULTI_TORCH: Tuple = (3, STD_IMG_SIZE, STD_IMG_SIZE)