import click
import datetime
from typing import Optional, Sequence, Any


class EnhancedDate(click.DateTime):
    def __init__(self, formats: Optional[Sequence[str]] = None):
        super().__init__(formats)
        self.formats += ["today"]  # works out well here

    def convert(self, value: Any, param: Optional["Parameter"], ctx: Optional["Context"]) -> Any:
        # we'll handle the "today" case ourself
        if value is None or value == "today":
            # return datetime.date.today()
            return "today"

        # we'll let click handle all the other stuff
        return super().convert(value, param, ctx)

    def __repr__(self):
        return "whatever"


@click.command()
@click.option("--newdate", type=EnhancedDate())
def cli(newdate):
    print(newdate)
    print(type(newdate))


cli()
