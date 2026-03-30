import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        max_z = z[0]
        for i in z:
            if i>max_z:
                max_z=i
        
        e = []
        for ele in z:
            e.append(np.exp(ele-max_z))
        total_sum = sum(e)

        probs = []
        for ele in e:
            prob = ele/total_sum
            probs.append(round(prob,4))
        return probs