import gym
import time

# Create the Mountain Car environment with render mode
env = gym.make('MountainCar-v0', render_mode='human')

# Reset the environment to its initial state
observation = env.reset()

try:
    for _ in range(300):
        env.render()  # Render the environment
        position, velocity = observation
        env.step(env.action_space.sample())  # Take a random action
        time.sleep(0.1)  # Add a slight delay to make the rendering smoother

except KeyboardInterrupt:
    print("Environment rendering interrupted by user")

finally:
    env.close()  # Close the rendering window
