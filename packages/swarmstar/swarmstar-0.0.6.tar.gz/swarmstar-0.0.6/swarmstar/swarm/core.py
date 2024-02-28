from typing import List, Union

from swarmstar.swarm.types import SwarmConfig, SwarmOperation, SpawnOperation, NodeEmbryo
from swarmstar.utils.swarm_utils.blocking_operations.main import blocking
from swarmstar.utils.swarm_utils.failure_operations.main import failure
from swarmstar.utils.swarm_utils.spawn_operations.main import spawn
from swarmstar.utils.swarm_utils.termination_operations.main import terminate

class Swarmstar:
    def __init__(self, swarm: SwarmConfig):
        self.swarm = swarm
        
    def spawn_root(self, goal: str) -> SpawnOperation:
        """
        Create the first spawn operation for the swarm.
        """
        root_spawn_operation = SpawnOperation(
            node_embryo=NodeEmbryo(
                action_id='swarmstar/actions/reasoning/decompose_directive',
                message=goal
            )
        )
        return root_spawn_operation
    
    def execute(
        self, swarm_operation: SwarmOperation
    ) -> Union[List[SwarmOperation], None]:
        """
        This function is the main entry point for the swarmstar library. It takes in a swarm configuration and a swarm operation
        and returns a list of swarm operations that should be executed next.
        """
        operation_mapping = {
            "spawn": spawn,
            "blocking": blocking,
            "terminate": terminate,
            "node_failure": failure,
        }

        if swarm_operation.operation_type in operation_mapping:
            output = operation_mapping[swarm_operation.operation_type](
                self.swarm, swarm_operation
            )
        else:
            raise ValueError(
                f"Unknown swarm operation type: {swarm_operation.operation_type}"
            )
        if isinstance(output, tuple):
            output = list(output)
        if not isinstance(output, list) and output is not None:
            output = [output]
            
        return output
