from argparse import ArgumentParser
from xai_components.base import SubGraphExecutor, InArg, OutArg, Component, xai_component, parse_bool
from xai_components.xai_utils.utils import Print, ConcatString

@xai_component(type='xircuits_workflow')
class HelloTutorial(Component):

    def __init__(self):
        super().__init__()
        self.__start_nodes__ = []
        self.c_0 = ConcatString()
        self.c_1 = Print()
        self.c_0.a.value = 'Hello '
        self.c_0.b.value = 'Xircuits!'
        self.c_1.msg.connect(self.c_0.out)
        self.c_0.next = self.c_1
        self.c_1.next = None

    def execute(self, ctx):
        for node in self.__start_nodes__:
            if hasattr(node, 'init'):
                node.init(ctx)
        next_component = self.c_0
        while next_component is not None:
            next_component = next_component.do(ctx)

def main(args):
    import pprint
    ctx = {}
    ctx['args'] = args
    flow = HelloTutorial()
    flow.next = None
    flow.do(ctx)
if __name__ == '__main__':
    parser = ArgumentParser()
    args, _ = parser.parse_known_args()
    main(args)
    print('\nFinished Executing')