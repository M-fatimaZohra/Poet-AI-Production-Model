from agents import Runner, set_tracing_disabled
from my_agents.poet import poet



set_tracing_disabled(True)



poetAI_history = []
while True:
    input_prompt = input("Enter the initial prompt for the Poet AI: ")
    if input_prompt.strip() == "":
          
          break
    poetAI_history.append({"role": "user", "content": input_prompt })
   
    result = Runner.run_sync(poet, poetAI_history)
    print(result.final_output)
    poetAI_history.append({"role": "assistant", "content": result.final_output})


    
     