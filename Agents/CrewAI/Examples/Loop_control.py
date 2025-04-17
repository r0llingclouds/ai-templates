from crewai.flow.flow import Flow, listen, router, start, or_
from pydantic import BaseModel

# Example flow that loops a number of times

class LoopState(BaseModel):
    counter: int = 0
    max_iterations: int = 3  # Set to 3 iterations

class LoopFlow(Flow[LoopState]):
    @start("start")
    def start_method(self):
        print("Starting the loop flow")
        print(f"Counter: {self.state.counter}")
        return "start_done"  # Trigger the router

    @listen(or_("start_method", "route_increment_done")) # You could shorten it by 1) removing route_increment and listening to increment_counter or even more 2) by removing increment_counter and listening directly to "continue" at check_iteration
    def pre_check(self):
        return "next_step"  # Trigger the router

    @router(pre_check)
    def check_iteration(self):
        print(f"Checking iteration {self.state.counter}")
        if self.state.counter >= self.state.max_iterations:
            return "end"  # End after 3 iterations
        else:
            return "continue"  # Continue the loop

    @listen("continue")
    def increment_counter(self):
        print(f"Iteration {self.state.counter}")
        self.state.counter += 1
        return "route_increment_done"  # Go back to start method

    @router(increment_counter)
    def route_increment(self):
        print(f"Routing back to pre check")
        return "route_increment_done"  # Go back to start method

    @listen("end")
    def end_method(self):
        print(f"Loop completed after {self.state.counter} iterations!")

flow = LoopFlow()
flow.kickoff()
