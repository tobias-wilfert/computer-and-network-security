import typer
from typing import Optional
from caesar_cipher import *

app = typer.Typer()


@app.command()
def caesar(message: str, k: int = typer.Option(3, help="Key for the cipher"),
           should_encode: Optional[bool] = typer.Option(True, "--encode/--decode", "-e/-d",
           help="Specifies if MESSAGE should be encoded or decoded "),
           remove_spaces: bool = typer.Option(False, "--remove_spaces/ ", "-rs/ ",
           help="Indicates if spaces should be retained in the ciphertext"),):
    """
    Encodes/Decodes a message using the caesar cipher
    """
    if should_encode:
        try:
            typer.echo(f"📝 {typer.style('Message:', bold=True)} {message}")
            typer.echo(f"✉️ {typer.style('Ciphertext:', bold=True)} {encode_caesar_cipher(message, k, remove_spaces)}")
        except ValueError:
            typer.secho("💥 Couldn't cipher message, make sure the message only contains letters and spaces.", fg=typer.colors.RED)
    else:
        try:
            typer.echo(f"✉️ {typer.style('Ciphertext:', bold=True)} {message}")
            typer.echo(f"📝 {typer.style('Message:', bold=True)} {decode_caesar_cipher(message, k)}")
        except ValueError:
            typer.secho("💥 Couldn't decipher text, make sure the ciphertext only contains letters and spaces.", fg=typer.colors.RED)

@app.command()
def general_substitution():
    typer.echo("Yet to co")

if __name__ == "__main__":
    app()
