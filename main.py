class CallCenter:

    def __init__(self, list_of_taxis, client_positions, client_destinations, time_limit, client_prefered_start_time_list):
        self.fleet = list_of_taxis
        self.taxi_busy_status = None
        self.open_clients = None
        self.time_limit = time_limit
        self.client_prefered_start_time_list = client_prefered_start_time_list
        
        self.client_positions = client_positions
        self.client_destinations = client_destinations

        self.current_time = 0
        self.list_of_rewards # TODO

        self.time_when_taxis_are_free = [0, 0] # todo
        self.total_reward = 0
        

    def initialise_taxis(self):
        self.taxi_busy_status = [0 for _ in range(len(self.fleet))] # 0 - free, 1 - allocated
        self.open_clients = [1 for _ in range(len(self.client_positions))]

    def update_all_taxis_time_to_complete(self, expection_taxi, quickest_time):
        for taxi in fleet:
            taxi.time_to_complete -= quickest_time



    def allocate_taxis(self):

        while sum(open_clients) > 0:
            # we want to allocate all taxis to clients, and have busy statuses 1
            while sum(self.taxi_busy_status) != len(self.taxi_busy_status):
                # match best client to best taxi
                max_reward_so_far = 0
                best_taxi_idx = 0
                best_client_idx = 0 
                for taxi_idx, taxi in enumerate(fleet):
                    # pass if busy
                    if taxi_busy_status[taxi_idx] == 1:
                        continue
                    taxi_max_reward = max(taxi.list_of_ratios) # TODO: in Taxi Class
                    if taxi_max_reward > max_reward_so_far:
                        max_reward_so_far = taxi_max_reward
                        best_taxi_idx = taxi_idx
                        best_client_idx = taxi.best_client_idx # TODO: in Taxi Class
                taxi_busy_status[taxi_idx] = 1
                taxi.time_to_complete = taxi.client_completion_time_list[best_client_idx]
                open_clients[best_client_idx] = 0
                
                # nullify clients if out of time


            # free up the earliest taxi
            quickest_time = 999999999
            for taxi in fleet:
                if taxi.time_to_complete <= quickest_time:
                    quickest_time = taxi.time_to_complete

            for taxi_idx, taxi in enumerate(fleet):
                if taxi.time_to_complete == quickest_time:
                    taxi_busy_status[taxi_idx] = 0
            
            self.update_all_taxis_time_to_complete(quickest_time):


class Taxi:

    def __init__(self, open_clients, client_positions, client_destinations, location, time_limit, client_prefered_start_time_list):
        self.list_of_rewards = []
        self.open_clients = open_clients
        self.location = location
        
        self.client_positions = client_positions
        self.client_destinations = client_destinations
        
        self.distance_to_clients = None
        self.time_to_complete_list = None

        self.current_time = current_time
        self.time_limit = time_limit

        self.client_prefered_start_time_list = client_prefered_start_time_list

        self.nunzio
        self.list_of_ratios = None

    def initalise_taxi(self):
        self.set_distance_to_client()
        self.set_time_to_complete()
        self.update_rewards()
    
    def update_rewards(self):
        for idx, client in enumerate(open_clients):
            reward = 0
            if client == 1:
                distance = self.distance_to_clients[idx] + self.time_to_complete_list[idx]

            if (self.time_limit - self.current_time) >= distance:
                reward += distance
                if self.current_time + self.distance_to_clients[idx] <= client_prefered_start_time_list[idx]:
                    reward += bonus
            self.list_of_rewards.append(reward)

    # TODO: def when to updat rewards again.


    def set_distance_to_client(self):
        distance_to_clients = [ abs(self.location[0] - client_location[0]) + 
                                abs(self.location[1] - client_location[1]) 
                                for idx, client_location in enumerate(client_positions)]
        

    def set_time_to_complete(self):
        time_to_complete = [ abs(client_destination[0] - client_positions[idx][0]) + 
                                abs(client_destination[1] - client_positions[idx][1]) 
                                for idx, client_destination in enumerate(client_destinations)]










#                 taxi.list_of_rewards
#                 # take a taxi closest to finish
#                 # 
#                 # when delivered free up the taxi


            
#             '''
#             Drive the client: vs. Drive all clients
#             - change time 
#             - change time of all the other taxi

#             nullify the positions of the client 
#             nullify the client_destinations'''
            
#             # get the reward
#             self.total_reward += 1
#             # change the current time : TODO
            
#             ''' 
#             this function should take into account the time
#             spended by the taxis. before the next ride '''
            
#             # TODO: change ratios for the taxi when finished

#             taxi_idx = min(time_when_taxis_are_free)
#             self.fleet

#             earliest_taxi_that_finish = 
#             self.current_time += earliest_taxi.

#             self.terminate_if_no_time_left()
        

#     # TODO: YELDOS
#     def choose_clients(self):
#         # a taxi that will be free next
#         best_taxi_so_far_idx = 0
#         maximum_ratio_so_far = 0
#         for idx in range(len(fleet)):
#             # if taxi is free
#             if not fleet[idx].is_allocated == True:
#                 # if the reward of this free taxi is maximum than prev.
#                 max_reward = max(fleet[idx].best_ratios)
#                 if max_reward > maximum_so_far:
#                     maximum_ratio_so_far = max_reward
#                     best_taxi_so_far_idx = idx
#         return fleet[idx]

#     # TODO: YELDOS
#     def drive_all_taxis(self, taxi):
#         # change the time when he will be free
#         set_time_when_taxis_are_free(self, taxi)

#     # DONE
#     def set_time_when_taxis_are_free(self, taxi):
#         ### # take the index of the given taxi # idx = self.fleet.index(taxi)
#         # Change the time of all taxis by to the next closest driving completion
#         self.time_when_taxis_are_free = [t + taxis.time_to_complete
#                                           for t in  self.time_when_taxis_are_free]
#         self.current_time += taxis.time_to_complete

#     def recalculate_rewards(self, clients):
#         pass

#     def terminate_if_no_time_left(self):
#         pass


# class Taxi:

#     def __init__(self):

#         self.current_step = 0 # done
#         self.location = (0, 0) # done
        
#         self.list_of_rewards = CallCenter(). #TODO: ANTON
#         self.list_of_earliest_finishes = [] #TODO: NUNZIO
#         self.best_ratios = [] # done

#         self.is_allocated = False # done
#         self.earned_reward = 0 # done
        
#         self.most_valuable_client_idx = 0 # done
        
#         # TODO:
#         self.steps_to_complete = 

#     def drive(self):
#         calculate_most_valueable_client()
#         idx = self.most_valuable_client_idx

#         # move the taxi
#         self.current_step += list_of_earliest_finishes[idx]
#         # close the client
#         list_of_earliest_finishes[idx] = 0
#         list_of_rewards[idx] = 0

#     def calculate_most_valueable_client(self):
#         self.best_ratio = [ float(r / list_of_earliest_finishes) for idx, r in enumerate(list_of_rewards)]
#         self.most_valuable_client_idx = best_ratio.index(max(best_ratio))

# if "__main__" == __name__:
#     no_taxis = 2
#     taxis = [Taxi() for _ in range(no_taxis)]
#     client_positions = []
#     client_destinations = []
    
#     c = CallCenter(taxi)
#     c.initialise_taxis()



