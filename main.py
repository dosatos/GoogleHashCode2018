class CallCenter:

    def __init__(self, list_of_riders, client_positions, client_destinations):
        self.fleet = list_of_riders
        self.client_positions = client_positions
        self.client_destinations = client_destinations
        self.current_time = 0
        # self.list_of_rewards

        self.time_when_finished = [0, 0] # todo

    def recalculate_rewards(self, clients):
        pass
        

    def allocate_rider(self):
        while sum(list_of_rewards) > 0:
            rider_idx = min(time_when_finished)
            earliest_rider_that_finish = 
            self.current_time += earliest_rider.

            self.terminate_if_no_time()

    def terminate_if_no_time(self):
        pass


class Rider:

    def __init__(self):

        self.current_step = 0 # done
        self.location = (0, 0) # done
        
        self.list_of_rewards = CallCenter(). # anton
        self.list_of_earliest_finishes = [] # nunzio
        self.best_ratio = [] # done

        self.is_allocated = False # done
        self.earned_reward = 0 # done
        
        self.most_valuable_client_idx = 0 # done
        
        # TODO:
        self.time_to_complete = 

    def step(self):
        calculate_most_valueable_client()
        idx = self.most_valuable_client_idx

        # move the rider
        self.current_step += list_of_earliest_finishes[idx]
        # close the client
        list_of_earliest_finishes[idx] = 0
        list_of_rewards[idx] = 0

    def calculate_most_valueable_client(self):
        self.best_ratio = [ float(r / list_of_earliest_finishes) for idx, r in enumerate(list_of_rewards)]
        self.most_valuable_client_idx = best_ratio.index(max(best_ratio))

if "__main__" == __name__:
    no_riders = 2
    riders = [Rider() for _ in range(no_riders)]
    client_positions = []
    client_destinations = []
    
    c = CallCenter(riders)



