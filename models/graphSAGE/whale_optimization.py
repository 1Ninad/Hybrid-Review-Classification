{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2a9a1bc5-56f6-43c6-8f5b-3039b05736fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Position: [44.74632577 52.88903842], Best Score: 0.07449276454973226\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "class WhaleOptimization:\n",
    "    def __init__(self, objective_function, num_whales, max_iter):\n",
    "        self.objective_function = objective_function\n",
    "        self.num_whales = num_whales\n",
    "        self.max_iter = max_iter\n",
    "        self.positions = np.random.rand(num_whales, 2)  # Random initial positions in 2D\n",
    "        self.best_position = None\n",
    "        self.best_score = float('inf')\n",
    "\n",
    "    def optimize(self):\n",
    "        for t in range(self.max_iter):\n",
    "            for i in range(self.num_whales):\n",
    "                score = self.objective_function(self.positions[i])\n",
    "                if score < self.best_score:\n",
    "                    self.best_score = score\n",
    "                    self.best_position = self.positions[i]\n",
    "            # Update positions (simplified version)\n",
    "            a = 2 - t * (2 / self.max_iter)\n",
    "            for i in range(self.num_whales):\n",
    "                r = np.random.rand(2)\n",
    "                self.positions[i] = self.best_position + a * r\n",
    "        return self.best_position, self.best_score\n",
    "\n",
    "# Example objective function\n",
    "def objective_function(position):\n",
    "    return np.sum(position ** 2)  # Minimize the sum of squares\n",
    "\n",
    "# Usage\n",
    "woa = WhaleOptimization(objective_function, num_whales=30, max_iter=100)\n",
    "best_position, best_score = woa.optimize()\n",
    "print(f'Best Position: {best_position}, Best Score: {best_score}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b959c157-79fd-4c78-81e8-05fb046f134f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
