class CallCenter:

    def __init__(self, list_of_riders, client_positions, client_destinations):
        self.fleet = list_of_riders
        self.client_positions = client_positions
        self.client_destinations = client_destinations
        self.current_time = 0
        self.list_of_rewards # TODO

        self.time_when_riders_are_free = [0, 0] # todo
        self.total_reward = 0

    def allocate_rider(self):
        while sum(list_of_rewards) > 0:
            # choose a rider
                # if free
                    # highest benefit
            rider = self.choose_rider()

            '''
            Drive the client: vs. Drive all clients
            - change time 
            - change time of all the other riders

            nullify the positions of the client 
            nullify the client_destinations'''
            drive_all_riders(rider)
            
            # get the reward
            self.total_reward += 1
            # change the current time : TODO
            
            ''' 
            this function should take into account the time
            spended by the riders. before the next ride '''
            

            rider_idx = min(time_when_riders_are_free)
            self.fleet

            earliest_rider_that_finish = 
            self.current_time += earliest_rider.

            self.terminate_if_no_time()
        

    # TODO: YELDOS
    def choose_rider(self):
        # a rider that will be free next
        # 
        best_rider_so_far_idx = 0
        maximum_reward_so_far = 0
        for idx in range(len(fleet)):
            # if rider is free
            if self.time_when_riders_are_free[idx] <= self.current_time:
                # if the reward of this free rider is maximum than prev.
                if self.list_of_rewards[idx] > maximum_so_far:
                    maximum_reward_so_far = self.list_of_rewards[idx]
                    best_rider_so_far_idx = idx
        return fleet[idx]

    # TODO: YELDOS
    def drive_all_riders(self, rider):
        # change the time when he will be free
        set_time_when_riders_are_free(self, rider)

    # DONE
    def set_time_when_riders_are_free(self, rider):
        ### # take the index of the given rider # idx = self.fleet.index(rider)
        # Change the time of all riders by to the next closest driving completion
        self.time_when_riders_are_free = [t + rider.time_to_complete
                                          for t in  self.time_when_riders_are_free]
        self.current_time += rider.time_to_complete

    def recalculate_rewards(self, clients):
        pass

    def terminate_if_no_time(self):
        pass


class Rider:

    def __init__(self):

        self.current_step = 0 # done
        self.location = (0, 0) # done
        
        self.list_of_rewards = CallCenter(). #TODO: ANTON
        self.list_of_earliest_finishes = [] #TODO: NUNZIO
        self.best_ratio = [] # done

        self.is_allocated = False # done
        self.earned_reward = 0 # done
        
        self.most_valuable_client_idx = 0 # done
        
        # TODO:
        self.steps_to_complete = 

    def drive(self):
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



