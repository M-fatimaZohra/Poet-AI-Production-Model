from agents import AgentHooks

class DebugHooks(AgentHooks):
    def before_tool_call(self, tool_call, agent, context):
        print(f"[HOOK] Tool used: {tool_call.tool.name}")
        print(f"[HOOK] Tool input: {tool_call.input}")
        return tool_call

debug_hooks = DebugHooks()
#this ni hao fine shyt is complicated, i will check it out later