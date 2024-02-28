
import click
import pkg_resources
from attr import evolve

from twisted.internet.task import react
from twisted.internet.defer import ensureDeferred

from wormhole.cli.public_relay import (
    RENDEZVOUS_RELAY as PUBLIC_MAILBOX_URL,
)

from ._proto import (
    _Config,
    wormhole_from_config,
    forward,
    frontend_accept_or_invite,
    WELL_KNOWN_MAILBOXES,
)
from ._tui import frontend_tui
from .messages import (
    LocalListener,
    RemoteListener,
)


# XXX need to replicate a bunch of "wormhole *" args?
# e.g. tor stuff, mailbox url, ..

# XXX there ar repeated args for "fowl" and "fowld" -- can we have a
# "common args" ... decorator? function?

@click.option(
    "--ip-privacy/--clearnet",
    default=False,
    help="Enable operation over Tor (default is public Internet)",
)
@click.option(
    "--mailbox",
    default=PUBLIC_MAILBOX_URL,
    help='URL for the mailbox server to use (or "default", "local" or "winden" to use well-known servers)',
    metavar="URL or NAME",
)
@click.option(
    "--debug",
    default=None,
    help="Output wormhole state-machine transitions to the given file",
    type=click.File("w", encoding="utf8"),
)
@click.command()
@click.pass_context
def fowld(ctx, ip_privacy, mailbox, debug):
    """
    Forward Over Wormhole Daemon

    Low-level daemon to set up and forward streams over Dilated magic
    wormhole connections
    """
    ctx.obj = _Config(
        relay_url=WELL_KNOWN_MAILBOXES.get(mailbox, mailbox),
        use_tor=bool(ip_privacy),
        debug_file=debug,
    )
    def run(reactor):
        return ensureDeferred(
            forward(
                reactor,
                ctx.obj,
            )
        )
    return react(run)


@click.option(
    "--ip-privacy/--clearnet",
    default=False,
    help="Enable operation over Tor (default is public Internet)",
)
@click.option(
    "--mailbox",
    default=PUBLIC_MAILBOX_URL,
    help='URL for the mailbox server to use (or "default" or "winden" to use well-known servers)',
    metavar="URL or NAME",
)
@click.option(
    "--debug",
    default=None,
    help="Output wormhole state-machine transitions to the given file",
    type=click.File("w", encoding="utf8"),
)
@click.option(
    "--local", "-L",
    multiple=True,
    help="Listen locally, connect remotely (accepted multiple times)",
    metavar="listen-port[:connect-port]",
)
@click.option(
    "--remote", "-R",
    multiple=True,
    help="Listen remotely, connect locally (accepted multiple times)",
    metavar="listen-port[:local-port]",
)
@click.option(
    "--allow",
    multiple=True,
    help="Accept a request to listen on a port (optionally which port to open on the far-side connection). Accepted multiple times",
    metavar="port[:connect-port]",
)
@click.group()
@click.pass_context
def fowl(ctx, ip_privacy, mailbox, debug, allow, local, remote):
    """
    Forward Over Wormhole, Locally

    Bi-directional streaming data over secure and durable Dilated
    magic-wormhole connections.

    This frontend is meant for humans -- if you want machine-parsable
    data and commands, use fowld (or 'python -m fowl')
    """
    def to_command(cls, cmd):
        if ':' in cmd:
            listen, connect = cmd.split(':')
        else:
            listen = connect = cmd
        # XXX ipv6?
        return cls(
            f"tcp:{listen}:interface=localhost",
            f"tcp:localhost:{connect}",
        )

    ctx.obj = _Config(
        relay_url=WELL_KNOWN_MAILBOXES.get(mailbox, mailbox),
        use_tor=bool(ip_privacy),
        debug_file=debug,
        commands=[
            to_command(LocalListener, cmd)
            for cmd in local
        ] + [
            to_command(RemoteListener, cmd)
            for cmd in remote
        ]
    )


@fowl.command()
@click.pass_context
@click.option(
    "--code-length",
    default=2,
    help="Length of the Wormhole code",
)
def invite(ctx, code_length):
    """
    Start a new forwarding session.

    We allocate a code that can be used on another computer to join
    this session (i.e. "fowl accept")
    """
    ctx.obj = evolve(ctx.obj, code_length=code_length)
    def run(reactor):
        return ensureDeferred(frontend_accept_or_invite(reactor, ctx.obj))
    return react(run)


@fowl.command()
@click.pass_context
@click.argument("code")
def accept(ctx, code):
    """
    Join an exiting forwarding session.

    This consumes an existing invite code (usually created by 'fow
    invite')
    """
    ctx.obj = evolve(ctx.obj, code=code)
    def run(reactor):
        return ensureDeferred(frontend_accept_or_invite(reactor, ctx.obj))
    return react(run)


@fowl.command()
@click.pass_context
def tui(ctx):
    """
    Run an interactive text user-interface (TUI)

    Allows one to use a human-readable version of the controller
    protocol directly to set up listeners, monitor streams, etc
    """
    def run(reactor):
        return ensureDeferred(frontend_tui(reactor, ctx.obj))
    return react(run)


@fowl.command()
def readme():
    """
    Display the project README
    """
    readme = pkg_resources.resource_string('fowl', '../../README.rst')
    # uhm, docutils documentation is confusing as all hell and no good
    # examples of "convert this rST string to anything else" .. :/ but
    # we should "render" it to text
    click.echo_via_pager(readme.decode('utf8'))


def _entry_fowl():
    """
    The entry-point from setup.py
    """
    return fowl()


def _entry_fowld():
    """
    The entry-point from setup.py
    """
    return fowld()


if __name__ == "__main__":
    _entry_fowl()
