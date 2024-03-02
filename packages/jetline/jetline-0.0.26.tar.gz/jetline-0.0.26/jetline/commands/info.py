import click
from colorama import Fore, Style

@click.command()
def main():
    """
    Print information about Kiper.
    """
    click.echo(f"{Fore.BLUE}What is Kiper?{Style.RESET_ALL}")
    click.echo("Kiper is a powerful, lightweight pipeline builder designed to simplify the creation and management of data processing pipelines.")
    click.echo("\n")

    click.echo(f"{Fore.BLUE}What can you do with Kiper?{Style.RESET_ALL}")
    click.echo("With Kiper, you can define, organize, and execute complex data processing workflows with ease.")
    click.echo("\n")

    click.echo(f"{Fore.BLUE}Documentation:{Style.RESET_ALL}")
    click.echo("For more information and detailed documentation, visit:")
    click.echo("https://kiper.readthedocs.io/en/latest/")
    click.echo("\n")

    click.echo(f"{Fore.BLUE}GitHub Repository:{Style.RESET_ALL}")
    click.echo("Find the Kiper source code and contribute on GitHub:")
    click.echo("https://github.com/yourusername/kiper")
    click.echo("\n")

    click.echo(f"{Fore.BLUE}PyPI Package:{Style.RESET_ALL}")
    click.echo("Kiper is available as a Python package on PyPI. Install it via pip:")
    click.echo("pip install kiper")
    click.echo("\n")


    click.echo(f"{Fore.BLUE}Welcome to Kiper!{Style.RESET_ALL}")
    click.echo("This command will guide you through setting up a new Kiper project.")
    click.echo("It will create the necessary project structure and files.")
    click.echo("\n")
    click.echo("To set up the project, run the following commands:")
    click.echo("1. kiper-setup")
    click.echo("2. Follow the prompts to provide project details.")
    click.echo("\n")

    click.echo(f"{Fore.BLUE}Creating a new pipeline!{Style.RESET_ALL}")
    click.echo("This command will create a new pipeline in your Kiper project.")
    click.echo("It will set up the necessary files and configurations.")
    click.echo("\n")
    click.echo("To create a new pipeline, run the following command:")
    click.echo("kiper-new-pipe")
    click.echo("\n")


if __name__ == '__main__':
    main()