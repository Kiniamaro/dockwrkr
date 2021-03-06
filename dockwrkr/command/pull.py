from dockwrkr import (Command)


class Pull(Command):

    def getShellOptions(self, optparser):
        optparser.add_option("-a", "--all", dest="allc",
                             help="Apply to defined containers", default=False, action="store_true")
        return optparser

    def getUsage(self):
        return "dockwrkr pull [options] CONTAINER..."

    def getHelpTitle(self):
        return "Pull the specified container(s)"

    def main(self):
        containers = self.args
        if not len(self.args) > 0 and not self.options.allc:
            return self.exitWithHelp("Please provide a container or use -a for all containers.")
        return self.core.pull(self.args, all=self.getOption('allc')) \
            .catch(self.exitError)
