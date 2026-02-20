"""
Hesperia v0.2 Release Invoker

This script serves as the main entry point for the v0.2 release of Hesperia. It orchestrates the entire workflow, which includes:

- Matrix traversal
- Logic validation
- Safeguard evaluation
- Path storage
- Observability telemetry

This MVP invoker wires together the components: matrix_run, context_rag, and hesperia_logic, while incorporating safeguards and tooling for Apple path, along with observability features for better integration with agents and automation.
"""

import matrix_run
import context_rag
import hesperia_logic
import safeguard
import apple_path_tooling
import observability


def main():
    """
    Main entry point of the Hesperia v0.2 invoker.
    
    This function executes the primary workflow, handling errors and gathering outputs.
    """
    try:
        # Step 1: Matrix traversal
        matrix_data = matrix_run.execute()
        
        # Step 2: Logic validation
        validation_result = hesperia_logic.validate(matrix_data)
        
        # Step 3: Safeguard evaluation
        if safeguard.evaluate(validation_result):
            
            # Step 4: Path storage
            apple_path_tooling.store(validation_result)
            
            # Step 5: Observability
            observability.log(validation_result)
            
            print("Workflow executed successfully.")
            # JSON output for integration
            import json
            print(json.dumps(validation_result))
        else:
            print("Safeguard evaluation failed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    main()