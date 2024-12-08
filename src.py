import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


# defining a grid to simulate the trail and error search and delayed rewards 
grid_cols=4
grid_rows=4

goal_state=[3,3]
start_state=[0,0]

actions=['up','down','left','right']


# function returns the next state based on the current  state and action , if the action is not possible then the state remains the same
def move(state,action):
    if action=='up' and state[0]>0:
        return [state[0]-1,state[1]]
    elif action=='down' and state[0]<grid_rows-1:
        return [state[0]+1,state[1]]
    elif action == 'left' and state[1]>0:
        return [state[0],state[1]-1]
    elif action == 'right' and state[1]<grid_cols-1:
        return [state[0],state[1]+1]
    
    return state


# simulation
def simulate(start,goal):
    visited=[]
    steps=0
    current_state=start
    actions_taken=[]

    unrefined_steps=0

    while(current_state!=goal):
        action=random.choice(actions)
        # print(action)
        # print(action)
        next_state=move(current_state,action)

        if next_state not in visited and next_state!=current_state:
            steps+=1
            visited.append(current_state)
            current_state=next_state
            actions_taken.append(action)

        unrefined_steps+=1


        if unrefined_steps>150:
            return -1,-1,visited
            
        
        

        if current_state==goal:
            break

    return steps,actions_taken,visited

# visualization of the actions taken by the agent to reach the goal 
def visualize(states_visited):
    print("Inside the visualise function")
    fig,ax=plt.subplots()
    ax.set_xlim(-0.5,grid_cols-0.5)
    ax.set_ylim(-0.5,grid_rows-0.5)
    ax.set_xticks(range(grid_cols))
    ax.set_yticks(range(grid_rows))
    ax.invert_yaxis()
    ax.grid(True)
    ax.scatter(goal_state[1],goal_state[0],color='red',s=100)
    agent, = ax.plot([], [], 'ro', label='Agent')


    def update(frame):
        state = states_visited[frame]
        print(state)
        agent.set_data([state[1]], [state[0]])
        return agent,

    ani = animation.FuncAnimation(
        fig, update, frames=len(states_visited), interval=500, blit=True
    )

    ax.legend()
    plt.show()

if __name__=="__main__":
    steps_took,actions_took,visited=simulate(start=start_state,goal=goal_state)
    if steps_took==-1 and actions_took==-1:
        print("Maze can't  be solved within specified time steps")
    else:
        print('steps took to reach the goal:',steps_took)
        print('actions taken:',actions_took)

    # visualize the process followed by agent 
    visualize(states_visited=visited)







