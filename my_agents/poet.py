from agents import Agent , AgentOutputSchema
from  my_conf.conf import MODEL
from my_tools.poet_tools import verses, save_poem_data 
from my_schema.blue_print import PoemSchema



#show what is the requirement to save poem in schema way
saving_requirement = Agent(
    name = "Saving Requirement",
    instructions="you are a agent that tell requrements to save poem in schema way and this is your only work, dont do anything else",
    model=MODEL,
    output_type=AgentOutputSchema(PoemSchema)
    )
  

#poem still need to be saved in json file, so we will use save_poem_data tool to save the poem with title and summary.
save_poem = Agent(
    name = "Save Poem",
    instructions= "You are a agent that only calls tool to saves the poem in the directory that is store in tool. show this data and in the end say saved\
                   -you can only use save_poem_data tool to save the poem with title and summary.\
                   -use generated poem as content, generated poem title as title, and given summary as short_summary.",
    model = MODEL,

    tools=[save_poem_data],
    
)

poet = Agent(
    name = "Poet AI",
    instructions= "you are PoetAI that generates poetry based on user prompts.\
                   -you can write poem in italian, english, russian, japanese, urdu and all asian languages.\
                   -you can use any format like haiku, sonnet, free verse, etc.\
                   -you can write in any gerne like romantic, horror, comedy, deep meaning, reality, childern poen etc.\
                   -you can write poem on any topic like love, nature, life, death, etc.\
                   -if user ask about your self, you can give breif about yourself and tallents. and you can also tell about your limitations.\
                   -if user ask about questions like who are you, what is your name, what can you do, etc. you can answer them.\
                   -if user ask questions related mathematics, science, history, or any unrelated query to Poetry etc. you cannot answer them no matter what, never suggest that you can also do that. just refuse by telling then you are not made for this subject\
                   -if user ask about their poetry, you can give them feedback and suggestions to improve their poetry if needed.\
                   -use heading title of poem at start of poem.\
                   -if user ask for stanza or central idea of poem, give them meaninful stanza or central idea of poem.\
                   -if user ask for summary of poem, give them summary of poem in one to five lines.\
                   -if user ask for your wellbeing, like hi how are you, how is your day, etc. you can answer them.\
                   -if user greets you, like hello, hi, how are you, etc. you can answer them.\
                   -if user ask about written poem like how many lines, how many stanzas, etc. you can answer them using verses tool.\
                   -if user ask to save poem, you can handoff to save_poem tool to save the poem with title and summary.",
    model = MODEL,
    tools=[verses, save_poem.as_tool("save_poem","This tool is used to save the poem with title and summary"), saving_requirement.as_tool("saving_requirement","This tool is used to tell requirements to save poem in schema way")],
    tool_use_behavior= "stop_on_first_tool",
    
    
   
    
)



# class Agent(
#     name: str,                                                                                                                             covered!
#     handoff_description: str | None = None,                                                                                                Basically covered!
#     tools: list[Tool] = list,                                                                                                              covered!
#     mcp_servers: list[MCPServer] = list,
#     mcp_config: MCPConfig = lambda : MCPConfig(),
#     instructions: str | ((RunContextWrapper[Any], Agent[Any]) -> MaybeAwaitable[str]) | None = None,                                       covered!
#     prompt: Prompt | DynamicPromptFunction | None = None,
#     handoffs: list[Agent[Any] | Handoff[Any, Any]] = list,                                                                                 covered!
#     model: str | Model | None = None,                                                                                                      covered!
#     model_settings: ModelSettings = ModelSettings,
#     input_guardrails: list[InputGuardrail[Any]] = list,
#     output_guardrails: list[OutputGuardrail[Any]] = list,
#     output_type: type[Any] | AgentOutputSchemaBase | None = None,                                                                          covered!
#     hooks: AgentHooks[Any] | None = None,                                                                                                  to complicated, will understand later. just know it do some debugging and logging
#     tool_use_behavior: StopAtTools | ToolsToFinalOutputFunction[Any] | Literal['run_llm_again', 'stop_on_first_tool'] = "run_llm_again",   covered!
#     reset_tool_choice: bool = True
# )


