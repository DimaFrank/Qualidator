import click
import os
from .inspectors.uniq import UniqInspector
from .inspectors.numeric import NumericInspector
from . import __version__
import shutil

@click.group()
@click.version_option(version=__version__, prog_name='qualidator', message='Qualidator CLI version: %(version)s')
def cli():
    """Qualidator CLI - manage data quality checks."""
    pass

@cli.command()
def init():
    """Initialize the Qualidations directory."""
    dir_path = './.qualidations'
    
    if os.path.exists(dir_path):
        click.secho(f"Directory '{dir_path}' already exists.", fg='yellow')
    else:
        try:
            os.mkdir(dir_path)
            click.secho("="*60, fg='cyan')
            click.secho("🎉 Welcome to QUALIDATOR! 🎉", fg='green', bold=True)
            click.secho("Your data quality journey begins here...", fg='blue')
            click.secho("-" * 60, fg='cyan')
            click.secho("📁 Directory '.qualidations' created successfully.", fg='green')
            click.secho("🛠  You can now start adding validations with:", fg='blue')
            click.secho("    qualidator add --name is_not_null", fg='white')
            click.secho("    qualidator add --name column_values_are_unique", fg='white')
            click.secho("    qualidator add --name column_max_is_between", fg='white')
            click.secho("="*60, fg='cyan')
        except Exception as e:
            click.secho(f"❌ Failed to create directory: {e}", fg='red')


@cli.command()
@click.option('--force', is_flag=True, help='Forcefully remove the Qualidations directory if it exists.')
def destroy(force):
    """Destroy the Qualidations directory."""
    dir_path = './.qualidations'
    
    if os.path.exists(dir_path):
        try:
            if force:
                shutil.rmtree(dir_path)
            else:
                os.rmdir(dir_path)
            click.secho("="*60, fg='red')
            click.secho("⚠ QUALIDATOR PROJECT DESTROYED ⚠", fg='red', bold=True)
            click.secho("The '.qualidations' directory has been removed.", fg='magenta')
            click.secho("We hope you enjoyed your stay. Come back soon!", fg='blue')
            click.secho("="*60, fg='red')
        except Exception as e:
            click.secho(f"❌ Failed to remove directory: {e}", fg='red')
    else:
        click.secho(f"Directory '{dir_path}' does not exist.", fg='yellow')




@cli.command(name='add')
@click.option('--name', required=True, help='Validation name to add.')
def add_validation(name):
    """Add validations to the suit."""

    if name.lower() == "is_not_null":
        column = click.prompt("Please enter the column name to check for NOT NULL")
        click.echo(f'✔ Will check that column "{column}" is not null.')

        query = (
            f"SELECT COUNT(*)\n"
            f"FROM ...\n"
            f"WHERE {column} IS NULL;\n"
        )
        with open(f'./.qualidations/{column.lower()}_{name.lower()}.sql', "w", encoding="utf-8") as f:
            f.write(query)

    elif name.lower() == 'column_values_are_unique':
        column = click.prompt("Please enter the column name to check for uniqueness")
        click.echo(f'✔ Will check that "{column}" column values are unique.')
        
        inspector = UniqInspector(column_name=column)
        query = inspector.column_values_are_unique()

        with open(f'./.qualidations/{column.lower()}_{name.lower()}.sql', "w", encoding="utf-8") as f:
            f.write(query)

    elif name.lower() == 'column_max_is_between':
        column = click.prompt("Please enter the column name to check for uniqueness")
        lower_bound = click.prompt("Please enter the lower bound:")
        upper_bound = click.prompt('Please enter the upper bound:')
        click.echo(f'✔ Will check that "{column}" column MAX values are between {lower_bound} and {upper_bound}')

        inspector = NumericInspector(column_name=column)
        query = inspector.column_max_is_between(lower_bound, upper_bound)

        with open(f'./.qualidations/{column.lower()}_{name.lower()}.sql', "w", encoding="utf-8") as f:
            f.write(query)
            
    else:
        click.secho(f"❗ Validation '{name}' is not supported yet.", fg='red')

@cli.command(name='remove')
@click.option('--all', 'remove_all', is_flag=True, help='Remove all validations.')
@click.option('--name', help='Name of the validation to remove.')
def remove_validation(remove_all, name):
    """Remove validation(s) from the suite."""
    dir_path = './.qualidations'

    if not os.path.exists(dir_path):
        click.secho("❌ Validation directory does not exist. Run `qualidator init` first.", fg='yellow')
        return

    if remove_all:
        deleted = 0
        for file in os.listdir(dir_path):
            if file.endswith('.sql'):
                os.remove(os.path.join(dir_path, file))
                deleted += 1
        click.secho(f"🗑 Removed {deleted} validation(s).", fg='green')
        return

    if name:
        file_path = os.path.join(dir_path, f"{name}.sql")
        if os.path.exists(file_path):
            os.remove(file_path)
            click.secho(f"🗑 Removed validation '{name}'.", fg='green')
        else:
            click.secho(f"⚠ Validation '{name}' not found.", fg='yellow')
        return

    click.secho("❗ Please provide either --all or --name option.", fg='yellow')



@cli.command(name='show')
def show_validations():
    """Show already added validations."""
    dir_path = './.qualidations'

    if not os.path.exists(dir_path):
        click.secho("❗ No validations found.", fg='yellow')
        click.secho("👉 Run `qualidator init` to create the project.", fg='blue')
        return

    sql_files = [f for f in os.listdir(dir_path) if f.endswith('.sql')]

    if not sql_files:
        click.secho("📁 Project initialized, but no validations found.", fg='yellow')
        click.secho("✨ You can add one using:", fg='blue')
        click.secho("   qualidator add --name is_not_null", fg='white')
        return

    click.secho("="*60, fg='cyan')
    click.secho("📋 VALIDATIONS IN YOUR PROJECT", fg='green', bold=True)
    click.secho("-"*60, fg='cyan')

    for i, file in enumerate(sql_files, 1):
        base_name = file.replace('.sql', '')
        click.secho(f"{i}. {base_name}", fg='white')

    click.secho("-"*60, fg='cyan')
    click.secho(f"✅ Total: {len(sql_files)} validation(s) ready to go!", fg='green')
    click.secho("💡 You can remove with:", fg='blue')
    click.secho("   qualidator remove --name your_validation_name", fg='white')
    click.secho("="*60, fg='cyan')




if __name__ == '__main__':
    cli()
