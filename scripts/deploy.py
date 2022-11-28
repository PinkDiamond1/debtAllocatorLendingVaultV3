import click
from ape.cli import network_option, NetworkBoundCommand
from ape import accounts, project

CAIRO_VERIFIER = "0xAB43bA48c9edF4C2C4bB01237348D1D7B28ef168"
CAIRO_PROGRAM_HASH = "0x18261fedf8bb9295db94450fdda4343f1b04d3ae08f198d079a0e178596f494"
# https://goerli.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161
def main():
    account = accounts.load("sacha")
    contract = project.DebtAllocator.deploy(CAIRO_VERIFIER, CAIRO_PROGRAM_HASH, sender=account)
    project.track_deployment(contract)

