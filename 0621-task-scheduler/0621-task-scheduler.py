import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Should always complete the task that has the most freq left.
        """
        taskFreq = {}
        while tasks:
            task = tasks.pop()
            if task not in taskFreq:
                taskFreq[task] = 0
            taskFreq[task] += 1
            
        remainingTasks = [(-t_cnt, t_id) for t_id, t_cnt in taskFreq.items()] # max heap
        coolingTasks = collections.deque() # (task, finishTime, remaining)
        cyclesElapsed = 0 # cycles same as time
        
        heapq.heapify(remainingTasks)
        
        while remainingTasks or coolingTasks:
          
            if coolingTasks and not remainingTasks:
                # currently idling; fast-forward to when next task is complete
                cyclesElapsed = coolingTasks[0][1]
            
            if coolingTasks and (coolingTasks[0][1] <= cyclesElapsed):
                cooledTaskId, coolEndTime, sameTaskRemaining = coolingTasks.popleft()
                
                heapq.heappush(remainingTasks, (-sameTaskRemaining, cooledTaskId) )
            
            
            t_cnt_neg, t_id = heapq.heappop(remainingTasks) # complete a task
            cyclesElapsed += 1
            
            if -t_cnt_neg > 1:
                # need to complete more of the same task -> track its cooldown so we can repeat
                coolingTasks.append( (t_id, cyclesElapsed + n, -t_cnt_neg - 1) )
        
        
        return cyclesElapsed