from argparse import ArgumentParser
from xai_components.base import SubGraphExecutor, InArg, OutArg, Component, xai_component, parse_bool
from xai_components.xai_agent.agent_components import AgentMakeToolbelt, AgentRun, AgentToolOutput, AgentDefineTool, AgentInit, AgentNumpyMemory
from xai_components.xai_openai.openai_components import OpenAIAuthorize
from xai_components.xai_utils.utils import Print, GetCurrentTime

@xai_component(type='xircuits_workflow')
class agent_example(Component):
    api_key: InArg[str]

    def __init__(self):
        super().__init__()
        self.__start_nodes__ = []
        self.c_0 = AgentNumpyMemory()
        self.c_1 = AgentInit()
        self.c_2 = AgentRun()
        self.c_3 = AgentMakeToolbelt()
        self.c_4 = Print()
        self.c_5 = AgentDefineTool()
        self.c_6 = GetCurrentTime()
        self.c_7 = AgentToolOutput()
        self.c_8 = OpenAIAuthorize()
        self.c_1.agent_name.value = 'hodlbot'
        self.c_1.agent_provider.value = 'openai'
        self.c_1.agent_model.value = 'gpt-4o-mini'
        self.c_1.agent_memory.connect(self.c_0.memory)
        self.c_1.system_prompt.value = 'You are a bot that helps people figure out time zones. \n\n{tool_instruction}\n\n{tools}\n\nExamples:\n\nUser:\nWhat is the current time in tokyo?\nAssistant:\nTOOL: get_current_time\nSystem:\n2024-03-07 23:35:00+0000\nAssistant:\nThe current time is 11:35 PM on March 7th.\n\n'
        self.c_1.max_thoughts.value = 5
        self.c_1.toolbelt_spec.connect(self.c_3.toolbelt_spec)
        self.c_2.agent_name.value = 'hodlbot'
        self.c_2.conversation.value = [{'role': 'user', 'content': 'What is the time in California'}]
        self.c_3.name.value = 'default'
        self.c_4.msg.connect(self.c_2.last_response)
        self.c_5.tool_name.value = 'get_current_time'
        self.c_5.description.value = 'Returns the current time in ISO format.'
        self.c_5.for_toolbelt.value = 'default'
        self.c_7.results.value = [self.c_6.time_str]
        self.c_8.api_key.connect(self.api_key)
        self.c_8.from_env.value = False
        self.c_0.next = self.c_3
        self.c_1.next = self.c_2
        self.c_2.next = self.c_4
        self.c_3.next = self.c_1
        self.c_4.next = None
        self.c_5.next = self.c_6
        self.c_6.next = self.c_7
        self.c_7.next = None
        self.c_8.next = self.c_0
        self.__start_nodes__.append(self.c_5)

    def execute(self, ctx):
        for node in self.__start_nodes__:
            if hasattr(node, 'init'):
                node.init(ctx)
        next_component = self.c_8
        while next_component is not None:
            next_component = next_component.do(ctx)

def main(args):
    import pprint
    ctx = {}
    ctx['args'] = args
    flow = agent_example()
    flow.next = None
    flow.api_key.value = args.api_key
    flow.do(ctx)
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--api_key', type=str)
    args, _ = parser.parse_known_args()
    main(args)
    print('\nFinished Executing')