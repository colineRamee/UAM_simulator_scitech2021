import tkinter as tk
from queue import Empty


class Symbol():
    def __init__(self,display, x ,y ,radius,status, ownship,multiple_planning_agents):
        self.display = display
        if multiple_planning_agents:
            self.radius = radius / 2
        else:
            self.radius = radius
        _radius = self.display.meter2pix(self.radius)
        x_ = self.display.meter2pix_coords(x)
        y_ = self.display.meter2pix_coords(y)
        self.ownship = ownship
        if ownship:
            self.icon = self.display.canvas.create_oval(x_ - _radius, y_ - _radius, x_ + _radius, y_ + _radius)
            self.color='green'
        else:
            self.icon = self.display.canvas.create_oval(x_ - _radius/10, y_ - _radius/10, x_ + _radius/10, y_ + _radius/10)
            self.color='black'
        if status == 'boom':
            self.color = 'red'
        self.change_color()

    def delete(self):
        self.display.canvas.delete(self.icon)

    def move(self,x,y,status):
        x_ = self.display.meter2pix_coords(x)
        y_ = self.display.meter2pix_coords(y)
        _radius = self.display.meter2pix(self.radius)
        if self.ownship:
            self.display.canvas.coords(self.icon, x_ - _radius, y_ - _radius, x_ + _radius, y_ + _radius)
        else:
            self.display.canvas.coords(self.icon, x_ - _radius/10, y_ - _radius/10, x_ + _radius/10, y_ + _radius/10)
        if status == 'boom' and self.color is not 'red':
            self.color = 'red'
            self.change_color()
        elif status == 'ok':
            if self.ownship and self.color is not 'green':
                self.color = 'green'
                self.change_color()
            elif not self.ownship and self.color is not 'black':
                self.color = 'black'
                self.change_color()

    def change_color(self):
        self.display.canvas.itemconfig(self.icon,outline=self.color)


class Display():
    def __init__(self, update_queue,length_arena,multiple_planning_agents=True,display_update=200):
        self.root = tk.Tk()
        self.root.title("Simulation")
        self.root.resizable(True, False)
        self.root.aspect(1,1,1,1)
        self.canvas = tk.Canvas(self.root, width=700, height=700,borderwidth=0, highlightthickness=0)
        self.canvas.pack()
        self.border_ratio = 0.1
        self.length=length_arena
        self.multiple_planning_agents=multiple_planning_agents
        self.update_queue = update_queue
        self.display_update=display_update  # in ms how often to show the new position
        self.symbols = {}
        self.canvas.bind("<Configure>",self.create_border)

    def create_border(self,event):
        x0=self.meter2pix_coords(0)
        y0=self.meter2pix_coords(0)
        x1=self.meter2pix_coords(self.length)
        y1=self.meter2pix_coords(self.length)
        self.canvas.create_line(x0,y0,x0,y1)
        self.canvas.create_line(x0, y0, x1, y0)
        self.canvas.create_line(x1, y1, x0, y1)
        self.canvas.create_line(x1, y1, x1, y0)

    def meter2pix(self,x):
        width_dis=self.canvas.winfo_width()
        return (1-self.border_ratio)*width_dis*x/self.length

    def meter2pix_coords(self,x):
        width_dis = self.canvas.winfo_width()
        return self.border_ratio*width_dis/2 + (1-self.border_ratio)*width_dis * x / self.length

    def update(self):
        try:
            update_agents = self.update_queue.get(timeout=1.0)
        except Empty:
            print('nothing in the queue')
            self.root.quit()
            return
        agents_to_delete = []
        for agent_id, symbol in self.symbols.items():
            # if an agent is not present in the list, delete its representation from the canvas
            # otherwise we just update its position
            if agent_id not in update_agents.keys():
                symbol.delete()
                agents_to_delete.append(agent_id)
            else:
                x = update_agents[agent_id]['x']
                y = update_agents[agent_id]['y']
                status = update_agents[agent_id]['status']
                symbol.move(x,y,status)
        for agent_to_delete in agents_to_delete:
            self.symbols.pop(agent_to_delete)

        # If an agent did not exist before, create it
        for update_agent_id, update_agent in update_agents.items():
            if update_agent_id not in self.symbols:
                x = update_agent['x']
                y = update_agent['y']
                radius = update_agent['radius']
                status = update_agent['status']
                ownship= update_agent['ownship']
                symbol = Symbol(self,x,y,radius,status,ownship,self.multiple_planning_agents)
                self.symbols[update_agent_id] = symbol

        self.canvas.after(self.display_update, self.update)

    def run(self):
        self.update()
        self.root.mainloop()

