import click
import client
import pprint
import pdb


@click.command()
@click.option('--redash-url')
@click.option('--api-key', help="API Key")
@click.option('--dashboard-slug', help="Dashboard slug")
@click.option('--copy-prefix', help="Text to prefix to name of copied elements", default="Copy of")
def main(redash_url, api_key, dashboard_slug, copy_prefix):
    redash_client = client.Redash(redash_url, api_key, copy_prefix)
    redash_client.duplicate_dashboard(dashboard_slug)

if __name__ == '__main__':
    main()
