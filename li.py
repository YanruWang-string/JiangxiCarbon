import pandas as pd
import numpy as np


les = pd.read_json("les-miserables.json",orient='index')
print(pd.DataFrame(les))









