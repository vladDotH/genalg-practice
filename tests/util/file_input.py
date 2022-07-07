from src.util import file_input
from src.model.core.Region import Region

t = file_input('towns.txt')
print(Region(t))
