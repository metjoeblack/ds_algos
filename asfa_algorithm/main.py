import numpy as np
import matplotlib.pyplot as plt

# Set non-interaction, avoid UBuntu error.
import matplotlib
matplotlib.use('Agg') 


class ArtificialFishSwarm:
    def __init__(self, func, n_fish=50, max_iter=100, visual=2.5, step=0.3, crowd_factor=0.6):
        self.func = func
        self.n_fish = n_fish
        self.max_iter = max_iter
        self.visual = visual
        self.step = step
        self.crowd_factor = crowd_factor
        
        self.X = np.random.uniform(-10, 10, (n_fish, 2))
        self.Y = np.array([self.func(x) for x in self.X])
        
        self.best_X = self.X[np.argmin(self.Y)]
        self.best_Y = np.min(self.Y)
        self.history = []

    def distance(self, x1, x2):
        return np.linalg.norm(x1 - x2)

    def move_towards(self, current_x, target_x):
        """auxiliary function"""
        vector = target_x - current_x
        norm = np.linalg.norm(vector)
        
        if norm == 0:
            return current_x
            
        step_vector = (vector / norm) * np.random.rand() * self.step
        return current_x + step_vector

    def prey(self, current_fish_idx):
        current_x = self.X[current_fish_idx]
        current_y = self.Y[current_fish_idx]
        
        for _ in range(10):
            next_x = current_x + (np.random.rand(2) * 2 - 1) * self.visual
            next_y = self.func(next_x)
            
            if next_y < current_y:
                return self.move_towards(current_x, next_x)
        
        return self.random_move(current_fish_idx)

    def swarm(self, current_fish_idx):
        current_x = self.X[current_fish_idx]
        current_y = self.Y[current_fish_idx]
        
        neighbors = []
        for i in range(self.n_fish):
            if self.distance(current_x, self.X[i]) < self.visual:
                neighbors.append(i)
        
        if len(neighbors) > 0:
            center_x = np.mean(self.X[neighbors], axis=0)
            center_y = self.func(center_x)
            nf = len(neighbors)
            
            if (center_y / nf) < (self.crowd_factor * current_y):
                return self.move_towards(current_x, center_x)
        
        return self.prey(current_fish_idx)

    def follow(self, current_fish_idx):
        current_x = self.X[current_fish_idx]
        current_y = self.Y[current_fish_idx]
        
        neighbors = []
        min_y = float('inf')
        best_neighbor_idx = -1
        
        for i in range(self.n_fish):
            dist = self.distance(current_x, self.X[i])
            if dist < self.visual:
                neighbors.append(i)
                if self.Y[i] < min_y:
                    min_y = self.Y[i]
                    best_neighbor_idx = i
        
        if best_neighbor_idx != -1:
            nf = len(neighbors)
            if (min_y / nf) < (self.crowd_factor * current_y):
                return self.move_towards(current_x, self.X[best_neighbor_idx])
                
        return self.prey(current_fish_idx)

    def random_move(self, current_fish_idx):
        return self.X[current_fish_idx] + (np.random.rand(2) * 2 - 1) * self.step

    def run(self):
        for i in range(self.max_iter):
            new_X = np.zeros_like(self.X)
            for j in range(self.n_fish):
                new_pos_follow = self.follow(j)
                new_pos_swarm = self.swarm(j)
                
                if self.func(new_pos_follow) < self.func(new_pos_swarm):
                    new_X[j] = new_pos_follow
                else:
                    new_X[j] = new_pos_swarm
            
            self.X = new_X
            self.Y = np.array([self.func(x) for x in self.X])
            
            current_best_y = np.min(self.Y)
            if current_best_y < self.best_Y:
                self.best_Y = current_best_y
                self.best_X = self.X[np.argmin(self.Y)]
            
            self.history.append(self.best_Y)


if __name__ == "__main__":
    def target_function(x):
        return x[0] ** 2 + x[1] ** 2

    print("Running AFSA Optimization...")
    afsa = ArtificialFishSwarm(target_function, n_fish=30, max_iter=50)
    afsa.run()
    
    print(f"Optimal Solution: {afsa.best_X}")
    print(f"Minimum Value: {afsa.best_Y}")
    
    # save to picture
    plt.plot(afsa.history)
    plt.title("Optimization Process")
    plt.xlabel("Iteration")
    plt.ylabel("Cost Function Value")
    
    # save to current directory
    plt.savefig('result_asfa.png')
    print("Success! Plot saved as 'result_asfa.png'")

